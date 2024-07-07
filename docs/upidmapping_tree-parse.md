# __idmapping_yyyy_mm_dd.json 트리와 파싱__

#### 이 문서와 연관된 파일
/notebook/jupyters/uniprot_json.ipynb

</br>

* First Created : 2023/08/02
* Last Uploaded : 2023/08/02
* Revision info : yyyy/mm/dd Rev. 0.1

</br>

#### 목차
1. idmapping 결과물의 포맷
2. JSON 파일로 보는 트리구조
3. 원하는 데이터 파싱하는 법 (예시: Protein name)

</br>

#### See Also
네이버 블로그 : [내 블로그 홈 - Blue Ocean 을 찾아서][Ext1]

</br>

## 1. idmapping 결과물의 포맷

</br>

Uniprot 웹에서 ID mapping 후의 결과는 10 개의 포맷(format)을 지원하고 있는데 이 포맷을 피쳐(feature) 선택이 가능한지 혹은 전체 피쳐를 갖고 있는지에 따라 크게 두 분류로 나눌 수 있다.

</br>

__분류 1. 피쳐 선택을 할 수 있는 포맷__
    
    TSV, Excel

__분류 2. 전체 피쳐를 담고있는 포맷__

    FASTA (canocical), FASTA (canonical & isoform), JSON, XML, RDF/XML, TEXT, GFF, List, Embeddings

</br>

사실, 피쳐 선택을 할 수 있는 포맷은 사용자가 사용할 피쳐를 선택하고 나면 전체 피쳐를 가지고 있는 포맷에서 선택한 부분만 떼어서 다운로드 할 수 있게 하는 방식이다.

피쳐 선택을 할 수 있는 포맷은 TSV (Tab-seprated value, 탭으로 분리) 와 Excel 둘 뿐이다. 반면, 전체 피쳐를 담고있는 포맷은 8 종류의 포맷을 지원한다. canonical 단독과 isoform 병합 폼의 FASTA는 하나로 묶었다.

이 포맷들 중에서, 생물정보학에서 사용되어지는 FASTA 포맷은 parser 코드가 구글링하면 잘 나와있다. 이 문서에서는 범용 데이터 포맷으로 많이 사용되어지는 JSON을 다룰 것이다.

</br>

## 2. JSON 파일로 보는 트리구조

</br>

트리 (Tree) 는 데이터의 구조를 볼 수 있는 선형의 계층적 자료 구조이다.

</br>

> 유튜브에서 어떤 영상을 본 적이 있는데 내용은 이렇다... "컴퓨터 잘하는 척 하는법" 이런 뉘앙스의 제목이었고 일단 cmd 프롬트를 켜서 최상위 루트 까지 cd .. 으로 이동 후, tree 명령어를 치면 디렉터리가 프롬트에 쭈욱 출력이 되는데, 이 때 Ctrl+z 를 누르지 않는 이상 멈추지 않기 때문에 자판을 열심히 두드리면 된다... 이런 내용이었다.

</br>

cmd에서 tree 명령어를 입력했을 때 나오는 디렉터리의 선형적 계층 구조가 바로 이 문서에서 다룰 JSON 포맷의 트리 구조와 같다.

수 많은 피쳐를 가지고 있는 데이터의 구조를 트리를 이용해 파악할 수 있다. 약간 노가다 일 수 있으나 앞으로 계속 마주해야할 데이터라면 트리를 통해 익숙해지는 시간을 갖자.

이 절에서 Uniprot의 idmapping 결과에 대한 트리를 전부다 나열하지는 않을 것이며 그럴 필요도 없다. 데이터의 트리 구조를 보면 알겠지만, 기본적으로 딕셔너리 형태의 {키:값} 형태로 되어있고, 이 값 안에는 다시 딕셔너리의 형태이거나 리스트 형태로 존재하고 있다.

__Protein과 Gene Name, 그리고 Sequence를 중심으로 한 트리 구조를 아래에 표시했다.__
아래의 구조는 어떠한 명령어로 만든 것은 아니고 한단계씩 접근하며 만든 것이다. 이 부분은 3절에서 언급한다.

지금은 어떤 피쳐들이 포함되어 있는지를 보라.

```json
"""
# Uniprot .json file structure by keys

results
    {0}
    {
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
                    'value'
            'alternativeNames'
            [
            'fullName'
                'evidences'
                ['evidenceCode', 'source', 'id'],
                'value'
            ]
            'submissionNames'
            [
            'fullName'
                'evidences'
                ['evidenceCode', 'source', 'id']
                'value'
            ]
        'genes'
        [
        'geneName'
            'evidences'
            ['evidenceCode', 'source', 'id'],
            'value'
        ]
        'comments'
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
            'value'
            'length'
            'molWeight'
            'crc64'
            'md5'
        'extraAttributes'
    }
"""
```

이 트리구조는 모든 트리를 펼쳐놓은 것은 아니며 이 챕터에서 관심이 있는 부분인 protein, gene name과 sequence 에 대해서만 펼쳐놓았고 작성 편의상 딕셔너리와 리스트의 구분없이 대괄호와 탭으로 구분을 했기에 실제 구조는 조금 다른 점을 감안해 주길 바란다. (이 부분은 추후에 수정하겠다.)

uniprot idmapping 데이터 구조를 보고자 다음 두가지 방법을 사용할 수 있다.

#### 첫번째. VScode 왼쪽 패널 'Explorer'에서 Outline 보기.

1. VScode 왼쪽 패널의 'Explorer'에서 하단의 'Outline'을 이용한다.

- 먼저, 이 방법은 확장프로그램 설치 없이 사용할 수 있다.
- 이 Outline 은 json 이외의 마크다운(.md), 파이썬 (.py) 확장자에서도 적용된다. 그 파일의 구조를 한 눈에 볼 수 있는 VScode의 기본 탑재 기능이다.
- 'Collapse All' 버튼을 눌러서 모든 feature 들을 collapse 한 뒤, 단계별로 탐색할 수 있다.


#### 두번째. VScode 확장프로그램 'JSON'.

1. 확장 프로그램에서 JSON을 검색하여 Meezilla의 JSON을 설치한다.
2. json 파일을 오픈한 뒤, "Ctrl + Shift + P" 커맨드를 입력 후 Beautiful JSON을 사용한다.
3. Indent = 4, primitive types = keep 으로 설정한다.

- json을 가독성이 좋게 만들어주는 확장 프로그램.

</br>

## 3. 원하는 데이터 파싱하는 법 (예시: Protein name)

</br>

이 절에서는 uniprot idmapping의 json 포맷 형식의 결과물에서 protein name, gene name, 그리고 sequence 값을 추출하는 것을 예시로 삼고있다.

</br>

### 3.1. .json 데이터에서 Protein Name 구조

Protein Name 은 다음의 세 종류가 있다.
- Recommended Name ('recommendedName')
- Alternative Name ('alternativeNames')
- Submission Name ('submissionNames')

이때 __Protein은 위 세가지 이름들 중 최소 하나는 가진다.__

데이터를 정리하려다 보니 어떤 protein은 이름을 두 개 가지고 있었고 어떤 것은 하나만 그런데 세개의 이름을 가진 protein은 찾지 못했는데 '왜 Uniprot 에서는 좀 쉽게 하나의 이름만 제공해 주면 되지 왜 여러개를 지원하고 있을까?' 라는 생각이 들었다.

이에 대해서 [Uniprot Help][Ref1] 에서 답을 확인할 수 있다.

> __SwissProt__
> 
> The subsection consists of 2 categories and several subcategories of protein names and abbreviations. It always begins with the 'Recommended name'  
>
> __TrEMBL__
>
> This is why UniProtKB/TrEMBL entries usually have 'Submitted name' instead of 'Recommended name'.
> 
> There can be more than one 'Submitted name'. 'Submitted names' may later be improved by automatic annotation procedures (the label will then change from 'SubName' to 'RecName'), but if not, it remains as provided by the submitter until the entry is manually annotated and integrated to UniProtKB/Swiss-Prot.

#### 예시

아래 예시에는 SwissProt(sp) 단백질 1 개, TrEMBL(tr) 단백질 2 개(submission, auto-annotation) 에 대해서 json 형식의 proteinDescription 을 나타냈다. (일부 피쳐는 생략함.)

예시 파일 : [idmapping_2023_07_20.json][ex-json1]

__1. {67}: Q6P9L6__

- Swiss-Prot data
- RecommendedName과 alternativeNames 2 개를 가짐

```json
{
"from": "Q6P9L6",
"to": {
    "entryType": "UniProtKB reviewed (Swiss-Prot)",
    "primaryAccession": "Q6P9L6",
    "secondaryAccessions": [
        "O35065",
        "Q70MX5"
    ],
    "proteinDescription": {
            "recommendedName": {
                "fullName": {
                "value": "Kinesin-like protein KIF15"
                }
            },
            "alternativeNames": [
                {
                "fullName": {
                    "value": "Kinesin-like protein 2"
                }
                },
                {
                "fullName": {
                    "value": "Kinesin-like protein 7"
                }
                }
            ]
            }
    }  
}
```

__2. {0}: A0A075B5P9__

- TrEMBL 데이터
- Automatic annotation 이 되지 않은 entry
- RecommendedName 없으며 submissionNames 피쳐를 가짐

```json
{
    "from": "A0A075B5P9",
    "to": {
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "primaryAccession": "A0A075B5P9",
        "proteinDescription": {
          "submissionNames": [
            {
              "fullName": {
                "evidences"
                "value": "Immunoglobulin heavy variable 5-4"
              }
            }
          ],
          "flag": "Fragment"
        },
    }
}

```

__3. {6}: A0A1B0GSE5__

- TrEMBL 데이터
- Automatic annotation 된 entry
- SubmissionNames가 recommendedName으로 바뀌었고 alternativeNames 피쳐는 세 개의 값을 가짐

```json
{
    "from": "A0A1B0GSE5",
    "to": {
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "primaryAccession": "A0A1B0GSE5",
        "proteinDescription": {
          "recommendedName": {
            "fullName": {
              "value": "Ubiquitin carboxyl-terminal hydrolase CYLD"
            },
          },
          "alternativeNames": [
            {
              "fullName": {
                "value": "Deubiquitinating enzyme CYLD"
              }
            },
            {
              "fullName": {
                "value": "Ubiquitin thioesterase CYLD"
              }
            },
            {
              "fullName": {
                "value": "Ubiquitin-specific-processing protease CYLD"
              }
            }
          ]
        }
    }
}
```

### 3.2 Protein Name 데이터 Parsing

d





<br>

## 4. 이 문서의 향후 개선방향
- 개선점 1
- 개선점 2

<br>

## Reference
(Ref.X) 저자명 et al. 저널명 연도, 권(호):쪽수. doi:10.xxxx/xxxx.


[1] Uniprot protein names에 관한 도움말.

(2)


[Ref1]:https://www.uniprot.org/help/protein_names
[Ext1]:https://blog.naver.com/simhc0714
[ex-json1]:https://github.com/simhc0714/oreome/blob/main/example/idmapping_2023_07_20.json
