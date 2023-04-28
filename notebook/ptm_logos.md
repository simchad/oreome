# __Motif 분석을 위한 sequnce alignment__

#### /pyFiles/ptm_logos.py
* created : 2023/04/21

<br>

#### 목차
1. 번역 후 수정(변형)
2. Motif 분석
3. 어떻게 구현할 것인가? ptm_logos.py

<br>

#### See Also
네이버 블로그 : [내 블로그 홈 - Blue Ocean 을 찾아서][Ext1]

<br>

# 1. 번역 후 수정(변형)

> 번역 후 수정 이란?

번역후수정(PTM, post translational modification)은 단백질이 다양한 기능을 가지게 한다.

연구활동에 빗댄다면, 같은 연구자라도 주 분야가 다를 것인데, wet 실험을 하거나, dry를 한다던지 혹은 분석만 하는 것과 같이 같은 연구자이지만 역할이 다른 것처럼 (조금 넓은 범위의 예시임을 고려하라).

같은 단백질이지만 어느 부위에 PTM이 일어나는지에 따라 그것이 단일 PTM 혹은 다중 PTM에 의한 기능이 다양해지는 것이다.

<br>

> PTM의 종류와 연구 방향

잘 알려진 PTM 으로는 인산화 (Phosphorylation), 유비퀴틴화 (Ubiquitination), 아세틸화 (Acetylation) 등 여러 PTM들이 있고 이런 번역후수정이 어느 단백질의 어떤 부위에 일어나는 지는 질량분석기술을 중심으로 한 Global 및 IP (Immuno Precipitation) 단백체 분석을 통해 high-throughput 하게 profiling이 되고 있다.

지금까지 알려진 PTM site의 수는 phosphorylation이 35만개 이상, Ubiquitination이 3만개 이상이, 총 60만개 정도의 PTM site가 알려져있다(1).

다만 이제는, 단순히 profiling을 함으로써 high-impact journal에 실리는 것은 어렵고 이러한 번역후수정이 일어난 단백질의 역할을 규명하는 것이 큰 관심사가 되었다.

다행스럽게도, 이러한 PTM을 쓰거나 (Wirter), 읽거나 (Reader) 혹은 지우는 (Eraser) enzyme들이 어떤 motif를 선호하는지 알려져 있다.

<br>

# 2. Motif 분석

> Motif 분석 수행 도구

Motif 분석을 수행할 수 있는 tool은 랩바랩으로 대체로 정해져 있다.

본인이 알고 있는 툴로는 pLogo, WebLogo, IceLogo 이렇게 3가지가 있는데 pLogo가 쓰기도 쉽고 직관적인 UI를 가지고 있다.

<br>

> pLogo

pLogo를 이용한 Motif 분석을 위해서는 PTM site를 정렬해 줄 필요가 있다.

단백체 분석 이후에는 IP 샘플을 사용했을 때 1,000개 이상의 site 가 관측되므로 작업을 하기가 매우 번거롭다.

<br>

# 3. 어떻게 구현할 것인가? ptm_logos.py

이 파일을 실행하기 위해서는 다음 두 가지 패키지가 필요하다.

데이터 분석을 함에 있어서 pandas와 numpy는 꼭 알아 두셔라.

```python
# import packages
import pandas as pd
import numpy as np
```

<br>

> 매개변수

먼저 파라미터는 4개를 받는다.
* df_site : 이 매개변수는 (pandas.DataFrame) 형식이고, header는 상관 없다. 다만 다음의 형식으로 되어있어야 한다. `UniprotAC-ID_Site-number` 여기서 UniprotAC-ID 는 Uniprot Accession ID 이고 Site-number는 PTM이 일어난 단백질의 gene sequence에 대응하는 아미노산의 번호다.

    Example.<br>
    A8DUK4의 18 번째 아미노산에 PTM이 있더라 : A8DUK4_18 

* df_sequence : 매개변수는 (pandas.DataFrame) 형식이다. 이 부분은 추후에 uniprot API로 대체할 예정.

* d : 기준이 되는 아미노산 앞 뒤로 몇개를 남겨둘 것인지를 지정한다. (정수형, 기본값=7)

* aa : PTM이 일어난 아미노산의 종류. one letter code로 작성한다. 대소문자는 구분하지 않아도 된다.

<br>

> 이 코드는 다음의 동작으로 수행된다 (아주 간단하다).

1. df_site 에서 _(언더바, 언더스코어)를 기준으로 좌측은 entry (UnprotAC-ID) 이고 우측은 site 이다.

2. entry가 df_sequence 에서 매칭이 된 것에 한해서 try~ except 구문을 수행하며 모종의 이유로 해당 위치의 sequence 의 아미노산이 매개변수로 넘겨진 aa와 같지 않을 경우 NaN을 반환한다.

3. Sequence에서 PTM의 위치는 N-term, C-term, 가운데 이렇게 3가지의 경우가 있다. 이 가운데 PTM site가 N-term이나 C-term 등 말단에 가까울 경우. 특히, 지정한 아미노산으로부터 남겨 놓을 d 에 의해 sequence가 모자라는 경우는 빈칸을 채워 넣음으로 motif를 align 한다.

<br>

```python
# Generate Logos data. Test ~10 rows
def logo_align(df_site, df_sequence, d:int=7, aa='K'):
    # Initialize params
    aa = aa.upper()
    entries = []
    logo = []
    start = []
    end = []
    
    # 1. UniprotAC-ID_Site
    for (i, entry) in df_site.iterrows():
        entries.append(entry[0].replace('_', '_'+aa))
        ent_name, ent_site = entry[0].split('_')
        ent_site = int(ent_site)
        # 2. Match entry in reference_sequence.
        try :
            seq = df_sequence.loc[ent_name]['Sequence']
            # For ent_site on sequence residue is lysine (K) if not -> else
            if seq[ent_site-1] == aa:
                # 3. Cases.
                # 3.1. If site residue locates too close forward of sequence.
                if ent_site-d-1 < 0:
                    start.append(int(1))
                    space = ""
                    for i in range(d+1-ent_site):
                        space += " "
                    logo.append(space+seq[:ent_site+d])
                    end.append(ent_site+d)
                # 3.2. If site residue locates too close backward of sequence.
                elif ent_site+d > len(seq):
                    start.append(ent_site-d)
                    space = ""
                    for i in range(ent_site+d-len(seq)):
                        space+=" "
                    logo.append(seq[ent_site-d-1:]+space)
                    end.append(len(seq))
                # 3.3. Normal condition.
                else:
                    start.append(ent_site-d)
                    logo.append(seq[ent_site-d-1:ent_site+d])
                    end.append(ent_site+d)
            else:
                start.append("NaN")
                logo.append("")
                end.append("NaN")
        # ent_site on sequence is not lysine (K) it is other amino acid.
        except:
            start.append("NaN")
            logo.append("")
            end.append("NaN")
    # Organized DataFrame
    logos = pd.DataFrame(np.column_stack([entries, logo, start, end]), columns=['Entry', 'Logo', 'Start residue', 'End residue'])
    return logos
```

<br>

> 아래와 같이 수행하면 된다.

<br>

1. 주피터 노트북에서

```python
if __name__ == "__main__":
    # Load example files.
    site = pd.read_csv(filepath_or_buffer='../example/Acetyl(K)Sites.csv', encoding='utf-8')
    ref_sequence = pd.read_csv(filepath_or_buffer='../example/Reference_sequence.csv', index_col=0, encoding='utf-8')

    # Run
    logos = logo_align(df_site=site, df_sequence=ref_sequence)
    logos.to_csv(path_or_buf='../output/logos.csv', index=False, encoding='utf-8')

    # Show the first 5 rows
    print(logos.head())
```

<br>

2. Python 에서
```python
if __name__ == "__main__":
    # Load example files.
    site = pd.read_csv(filepath_or_buffer='example\Acetyl(K)Sites.csv', encoding='utf-8')
    ref_sequence = pd.read_csv(filepath_or_buffer='example\Reference_sequence.csv', index_col=0, encoding='utf-8')

    # Run
    logos = logo_align(df_site=site, df_sequence=ref_sequence)
    logos.to_csv(path_or_buf='.\output\logos.csv', index=False, encoding='utf-8')

    # Show the first 5 rows
    print(logos.head())
```

<br>

실행 결과

```bash
         Entry             Logo Start residue End residue
0  A8DUK4_K145  VAAALAHKYH                138         147
1   A8DUK4_K18  AVSGLWGKVNADEVG            11          25
2   A8DUK4_K67  KVKAHGKKVITAFND            60          74
3   A8DUK4_K96  LSELHCDKLHVDPEN            89         103
4  D3Z7X0_K535  RLGDDQLKVAKMELK           528         542
```

가운데 K (lysine)로 정렬되며 앞뒤로 7개의 아미노산이 위치해 있고 sequence 길이가 모자라다면 공백(" ")으로 잘 채워져서 출력된다.

이제 이 Logo 부분을 복사해서 pLogo 에 붙여넣기만 하면 된다.!

<br>

# 4. 향후 개선 방향
- Uniprot API를 이용해서 sequence 받아오는 기능.
- 예외 처리: protein이 deleted 혹은 merge 된 경우.
- Multiple alignment.

<br>

# Reference
(1) Kim et al. BMC Medical Genomics 2015, 8(Suppl 2):S7. doi:10.1186/1755-8794-8-s2-s7.
<br>
(2)


[Ext1]:https://blog.naver.com/simhc0714