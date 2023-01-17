## MQpy/jobs/README.md
> Since 2023.01.17. <br/>

###  Issues
>**proteingroups_basic.py**<br/>
- 실행하면, variables 탐색에 어려움.
- 경로명 설정시, 슬래시('/') 사용.

>**proteingroups_basic.ipynb**<br/>
- 셀 단위로 실행
- variables를 jupyter variables 패널로 볼 수 있음.
- jupyter variables panel 'data viewer' 유용.
- 경로명 설정 시, 역슬래시 두 개 ('\\') 사용. 역슬래시 한 개 사용시 unicodeescape 오류.

### Solution
> *.ipynb >>> *.py