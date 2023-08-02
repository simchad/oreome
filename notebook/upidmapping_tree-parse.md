# __idmapping_yyyy_mm_dd.json 트리와 파싱__

#### 이 문서와 연관된 파일
/notebook/jupyters/uniprot_json.ipynb

</br>

* First Created : 2023/08/02
* Last Uploaded : 2023/08/02
* Revision info : yyyy/mm/dd Rev. 0.1

</br>

#### 목차
1. idmapping 결과물의 확장자
2. JSON 파일로 보는 트리구조
3. 원하는 데이터 파싱하는 법 (예시: Protein name, Sequence)

</br>

#### See Also
네이버 블로그 : [내 블로그 홈 - Blue Ocean 을 찾아서][Ext1]

</br>

## 1. idmapping 결과물의 포맷

Uniprot 웹에서 ID mapping 후의 결과는 10 개의 포맷(format)을 지원하고 있는데 이 포맷을 피쳐(feature) 선택이 가능한지 혹은 전체 피쳐를 갖고 있는지에 따라 크게 두 분류로 나눌 수 있다.

__분류 1. 피쳐 선택을 할 수 있는 포맷__
    
    TSV, Excel

__분류 2. 전체 피쳐를 담고있는 포맷__

    FASTA (canocical), FASTA (canonical & isoform), JSON, XML, RDF/XML, TEXT, GFF, List, Embeddings

사실, 피쳐 선택을 할 수 있는 포맷은 사용자가 사용할 피쳐를 선택하고 나면 전체 피쳐를 가지고 있는 포맷에서 선택한 부분만 떼어서 다운로드 할 수 있게 하는 방식이다.

피쳐 선택을 할 수 있는 포맷은 TSV (Tab-seprated value, 탭으로 분리) 와 Excel 둘 뿐이다. 반면, 전체 피쳐를 담고있는 포맷은 8 종류의 포맷을 지원한다. canonical 단독과 isoform 병합 폼의 FASTA는 하나로 묶었다.

이 포맷들 중에서, 생물정보학에서 사용되어지는 FASTA 포맷은 parser 코드가 구글링하면 잘 나와있다. 이 문서에서는 범용 데이터 포맷으로 많이 사용되어 지는 JSON을 다룰 것이다.

</br>

## 2. JSON 파일로 보는 트리구조

트리 (Tree) 는 데이터의 구조를 볼 수 있는 선형의 계층적 자료 구조이다.

> 유튜브에서 어떤 영상을 본 적이 있는데 내용은 이렇다... "컴퓨터 잘하는 척 하는법" 이런 뉘앙스의 제목이었고 일단 cmd 프롬트를 켜서 최상위 루트 까지 cd .. 으로 이동 후, tree 명령어를 치면 디렉터리가 프롬트에 쭈욱 출력이 되는데, 이 때 Ctrl+z 를 누르지 않는 이상 멈추지 않기 때문에 자판을 열심히 두드리면 된다... 이런 내용이었다.

cmd에서 tree 명령어를 입력했을 때 나오는 디렉터리의 선형적 계층 구조가 바로 이 문서에서 다룰 JSON 포맷의 트리 구조와 같다.

수 많은 피쳐를 가지고 있는 데이터의 구조를 트리를 이용해 파악할 수 있다. 약간 노가다 일 수 있으나 앞으로 계속 마주해야할 데이터라면 트리를 통해 익숙해지는 시간을 갖자.

이 절에서 Uniprot의 idmapping 결과에 대한 트리를 전부다 나열하지는 않을 것이며 그럴 필요도 없다. 데이터의 트리 구조를 보면 알겠지만, 기본적으로 딕셔너리 형태의 {키:값} 형태로 되어있고, 이 값 안에는 다시 딕셔너리의 형태이거나 리스트 형태로 존재하고 있다.

__Protein과 Gene Name, 그리고 Sequence를 중심으로 한 트리 구조를 아래에 표시했다.__
아래의 구조는 어떠한 명령어로 만든 것은 아니고 한단계씩 접근하며 만든 것이다. 이 부분은 3절에서 언급한다.

```bash
"""
# Uniprot .json file structure by keys

results
    from
        Uniprot Accession ID
    to
        'entryType' : 'UniProtKB reviewed (Swiss-Prot)' OR 'UniProtKB unreviewed (TrEMBL)'
        'primaryAccession' : (Primary Accession ID)
        'uniProtkbId' : UniprotKB_MOUSE
        'entryAudit'
        'annotationScore'
        'organism'
        'proteinExistence'
        'proteinDescription'
            'recommendedName'
                'fullName'
                    'evidences'
                    ['evidenceCode', 'source', 'id'],
                    'value' # <-- ***
            'alternativeNames'
            [
            'fullName'
                'evidences'
                ['evidenceCode', 'source', 'id'],
                'value' # <-- ***
            ]
            'submissionNames'
            [
            'fullName'
                'evidences'
                ['evidenceCode', 'source', 'id']
                'value' # <-- ***
            ]
        'genes'
        [
        'geneName'
            'evidences'
            ['evidenceCode', 'source', 'id'],
            'value'
        ]
        'features'
        'keywords'
        'references' # number of N from ['references'].__len__() 
        [
        'citation'
        'referencePositions'
        'referencecomments'
        'evidences'
        ]
        'uniProtKBCrossReferences'
        'sequence'
            'value' # <-- ***
            'length'
            'molWeight'
            'crc64'
            'md5'
        'extraAttributes'
"""

```

> 소주제 (1)

내용 1

</br>

## 3. 원하는 데이터 파싱하는 법 (예시: Protein and Gene, Sequence)

> Protein Name

Protein Name 은 다음의 세 종류가 있다.
- Recommended Name ('recommendedName')
- Alternative Name ('alternativeNames')
- Submission Name ('submissionNames')

__Protein은 최소한 셋 중의 하나는 가진다.__ 이름이 없는 protein은 Search할 당시에 사용했던 FASTA가 현재의 DB와 맞지 않아 생기는 Accession ID의 문제로 보인다. 이 부분은 고민해보겠다.

context


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

## 4. 이 문서의 향후 개선방향
- 개선점 1
- 개선점 2

<br>

## Reference
(1) 저자명 et al. 저널명 연도, 권(호):쪽수. doi:10.xxxx/xxxx.

(2)


[Ext1]:https://blog.naver.com/simhc0714