# 사용자 패키지는 setup.py 로 관리하자.

#### 이 문서와 연관된 파일
/setup.py

</br>

#### C.U.R.D.
* Created : 2023/05/02
* Uploaded: 2023/05/18
* Revision: 2023/05/18
    
    소제목 1 추가 (2023/05/18)

    소제목 2 추가 (2023/mm/dd)

</br>

#### 목차
1. setup.py 도입을 고려해야할 때
2. setup.py 의 작성법과 유용한 메타데이터

</br>

#### See Also
네이버 블로그 : [내 블로그 홈 - Blue Ocean 을 찾아서][Ext1]

</br>

# 1. setup.py 도입을 고려해야할 때

> 패키징. 참조의 문제

프로젝트 초기에는 함수들이 같은 디렉터리에 있어서 쉽게 import 가 가능하다. 그러나 꾸준히 개밯을 하고 필요한 툴들을 만들다 보면, 함수들을 패키징 해야할 순간이 찾아온다.

패키징 자체는 쉽다. 하나의 파이썬 파일에 몰아 넣고 적당한 이름으로 저장하면 된다. 다만, 이 경우에도 몰아 넣은 파이썬 파일이 같은 디렉터리에 있다면 이 역시 임포트 하는 데 큰 어려움이 없다.

문제는 이 패키지들을 여러개의 폴더 구조로 만들면서부터 시작된다. 예를 들어 아래와 같은 트리 구조가 있다고 하자.

</br>

```bash
My_tool
|--tool_A
|   |--page_gel.py
|   |--transfer.py
|
|--tool_B
|   |--mk_gel.py
|
|--experiment.py
# Python3.3 부터는 __init__.py 가 없어도 패키지로 인식한다. 다만 하위 버전과의 호환성을 위해 던더 init을 관례상 만들어 준다.
```
</br>

웹 검색을 해보면 많은 경우에서 root 기준 하위 폴더 한 개 정도의 예시가 대부분인데 이 문서에서는 하위 폴더 두 개를 생각해 보자.

</br>

이 예시는 아래의 세가지 상황으로 정리될 수 있다.?

1. 같은 디렉터리의 패키지를 불러오는 경우.
2. 다른 디렉터리의 패키지를 불러오는 경우.
3. <b> 다른 디렉터리의 패키지에 포함된 함수를 사용하는 함수 (setup.py의 필요성).</b>

</br>

이 예시의 각 *.py 파일은 세 부분으로 구성되는데, (1) docstring 부분, (2) 함수 정의, 그리고 (3) 네임스페이스가 메인인 경우에 실행되는 함수 부분 이다.

</br>

1. 같은 디렉터리의 패키지를 불러오는 경우.</br>
   
    다시 말하지만, 같은 디렉터리 내에 있으면 import 패키지이름 하여 사용할 수 있다.

    ```python
    # transfer.py
    """
    tranfer.py

    This is the transfer.py
    """
    # 위의 큰따옴표 세개로 묶인 부분이 docstring(독스트링)이다.
    # 독스트링은 던더메서드 .__doc__ 으로 불러올 수 있다.

    import page_gel
    # page_gel은 transfer.py 기준으로 같은 디렉터리에 있다.
    # 같은 디렉터리의 패키지는 import (이름)으로 불러올 수 있다.

    def wet_transfer():
        # 이 함수는 불러온 page_gel의 docstring을 print 하는 함수다.
        print(page_gel.__doc__)

    if __name__ == "__main__":
        # 네임스페이스가 메인일 때 wet_transfer 함수를 실행한다.
        wet_transfer()
    ```
    transfer.py 파일을 실행하면, page_gel.py 파일의 독스트링이 출력된다.
    ```bash
    page_gel.py

    This is the page_gel.py
    ```
    <b><i>주의!</i></b>

    기초적인 것이기 때문에 여기서 딱 한번 언급하고 지나간다. transfer.py 를 실행한다는 것은 다음 두 가지 상황일 때 정상적으로 동작한다.

    (1) IDE 등에서 transfer.py 파일을 열어 직접 실행하는 경우.
    
    (2) 터미널에서 transfer.py 위치로 이동한 후 python transfer.py 명령으로 실행하는 경우.

    위치가 일치하지 않으면 아래의 에러가 발생한다.

    ```bash
    [Errno 2] No such file or directory
    ```

    지금 터미널의 경로가 해당 파일에 위치해 있지 않다면, cd 구문으로 디렉터리를 변경할 수 있다.

</br>

2. 다른 디렉터리의 패키지를 불러오는 경우.

    상대경로를 사용하여 불러올 수 있다.

    ```python
    # page_gel.py
    """
    page_gel.py

    This is the page_gel.py
    """
    from example.tool_B import mk_gel
    # page_gel을 기준으로 mk_gel의 상대경로는
    # /example/tool_B/mk_gel 이다.

    def sds_page():
        # mk_gel에 속한 make_gel 이라는 함수를 실행한다.
        mk_gel.make_gel()

    if __name__ == "__main__":
        sds_page()
    ```
    실행하면,

    ```bash
    Ingridients of Tris-glycine gel : 
    Add Tris-pH8.8, 30%-Acrylamide
    Add APS, 10%-SDS, TEMED
    ```
    가 출력될 것이다.

</br>

3. <b>다른 디렉터리의 패키지에 포함된 함수를 사용하는 함수 (setup.py의 필요성).</b>

    자... 지금부터 문제가 발생한다. 유용한 도구들을 만들고 이를 패키징해서 적당한 폴더에 정리했다고 생각해보자. 그것이 이번의 예제의 상황과 같다. 
    
    page_gel, transfer, 그리고 mk_gel 이라는 함수를 만들어서 종류와 상황에 맞게 적당한 폴더에 위치시켰다.

    그러고나서, experiment.py 라는 새로운 파일을 만들어 패키징한 함수를 불러와서 사용을 하려는데 작동을 하지 않는다.

    experiment.py 코드는 아래와 같다.

    ```python
    # experiment.py
    from example.tool_A import transfer
    # experiment를 기준으로 상대경로에서 transfer 를 불러온다.

    transfer.wet_transfer()
    # 불러온 패키지에서 wet_transfer() 란 함수를 사용한다.
    ``` 
    상대경로도 잘 기입했고 별문제 없다고 생각을 하겠지만
    
    실행하면,
    ```bash
    Traceback (most recent call last):
    File "c:\Users\user\Documents\GitHub\proteome-tool\example\experiment.py", line 2, in <module>
        from example.tool_A import transfer
    File "c:\users\user\documents\github\proteome-tool\example\tool_A\transfer.py", line 8, in <module>
        import page_gel
    ModuleNotFoundError: No module named 'page_gel'
    ```
    에러가 여러줄짜리가 떴는데. 본인은 처음에 적잖이 당황했다.

    지인이 함수들을 클래스에 넣는 것보다 패키징을 하는게 좋지 않을까라고 조언해준 이후 다 뜯어 고쳐가며 패키징을 열심히 해왔는데 실행이 안된다니... 나는 적잖이 당황했다. 정말.

    여기서 상대경로도 바꿔보고, 던더 init 파일도 수정해 보았지만 속시원한 방법은 setup.py 말고는 없었다. 깃허브를 보다보면 많은 개발자들이 setup.py 를 채택하고 있다 (최근 나온 것들 중에서 rosettacommons의 RFdiffusion도 setup.py를 채택하고 있다.)

    </br>

    > 일단 에러의 원인을 보자.

    </br>

    두번째 줄에서... 상대경로를 사용하며 transfer 는 잘 불러왔다만

    transfer.py의 8번째 줄인 import page_gel 부분에서 모듈이름이 page_gel 인게 없다는 에러다.

    experiment.py 가 실행되는 디렉터리를 기준으로는 page_gel 모듈이 없기 때문에 이런 오류가 발생한 것이다.

    해결방법은 의외로 간단한데, transfer.py 파일에서 import page_gel 부분을 아래처럼 바꿔어 주면 된다.

    ```python
    from . import page_gel
    ```

    다시, experiment.py를 실행해 보면...

    ```bash
    page_gel.py

    This is the page_gel.py
    ```

    page_gel의 docstring이 잘 출력된다.

    <b>그런데</b> 위의 방식으로 코드를 바꾸었을 때 transfer.py는 실행이 될까?

    정답은 "<u>NO</u>" 다. 이 상태에서 transfer.py를 실행해보면...

    ```bash
    Traceback (most recent call last):
    File "c:\Users\user\Documents\GitHub\proteome-tool\example\tool_A\transfer.py", line 9, in <module>
        from . import page_gel
    ImportError: attempted relative import with no known parent package
    ```

    임포트 에러가 떠버린다. 상위 폴더가 뭔지 모르는 상태에서 상대 임포트를 시도한다는 것이다.

    </br>

    ### 그럼 어떻게 하란 말인가? transfer.py 를 원래대로 고치면 experiment.py 에서 에러가 발생할 텐데.

    </br>

    ### 여기서~ "setup.py" 를 사용하면 신세계가 열린다.

</br>

> setup.py 를 사용하면 보여질 신세계.

1. py 파일 서로 간에 import 가 쉽게 바뀜.

2. 다른 사용자가 배포판을 사용할 경우, 구동에 필요한 패키지들을 자동으로 설치할 수 있음.

</br>

# 2. setup.py 의 작성법과 유용한 메타데이터




<br>

내용 1

```python
# python preference
import pandas as pd
import numpy as np
```

<br>

내용 2

<br>

실행 결과
```bash
# bash preference
import pandas as pd
import numpy as np
```

<br>

내용 3



<br>

# 4. 향후 개선점
- 개선점 1
- 개선점 2

<br>

# Reference
(1) 저자명 et al. 저널명 연도, 권(호):쪽수. doi:10.xxxx/xxxx.

(2)


[Ext1]:https://blog.naver.com/simhc0714