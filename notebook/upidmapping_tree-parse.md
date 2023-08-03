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

이 포맷들 중에서, 생물정보학에서 사용되어지는 FASTA 포맷은 parser 코드가 구글링하면 잘 나와있다. 이 문서에서는 범용 데이터 포맷으로 많이 사용되어 지는 JSON을 다룰 것이다.

</br>

---

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

```bash
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
    {1}
    {2}
    .
    .
    .
    {N}
"""
```

이 트리구조는 편의상 딕셔너리와 리스트를 구분없이 대괄호와 탭으로 구분을 했기에 실제 구조는 조금 다른 점을 감안해 주길 바란다. 또한 데이터 마다 특정 피쳐들의 유무가 있을 수 있다.

json 파일을 VScode에서도 지원하고 있다. json 코드를 짜임새 있게 보여주는 확장프로그램도 있는데, uniprot data가 원체 피쳐가 많고 아무튼 그래서 잘 동작하지는 않는다.

그래도 걱정하기는 이르다. VScode의 문서 개요 창에서 이 json 파일의 계층적 구성의 일부를 제공해주기 때문에 개략적인 데이터 구성을 파악할 수 있다.

</br>

---

</br>

## 3. 원하는 데이터 파싱하는 법 (예시: Protein and Gene name, Sequence)

</br>

이 절에서는 uniprot idmapping의 json 포맷 형식의 결과물에서 protein name, gene name, 그리고 sequence 값을 추출하는 것을 예시로 삼고있다.

</br>

### 3.1. Protein Name

Protein Name 은 다음의 세 종류가 있다.
- Recommended Name ('recommendedName')
- Alternative Name ('alternativeNames')
- Submission Name ('submissionNames')

이때 __Protein은 최소한 위의 세가지 이름들 중의 하나는 가진다.__

Q. Uniprot 에서는 좀 쉽게 하나의 이름만 제공해 주면 되지 왜 여러개를 지원하고 있을까?

A.

화합물에 이름을 붙이는 IUPAC 이름과 관용명 같은 관계처럼 어떤 단백질의 경우에는 이름이 여러개를 가진 것도 있다. 이 때, Uniprot에서는 사용하기를 추천하는 이름으로 Recommended Name을 사용하고, 그 외의 이름은 Alternative Name 으로 정하고 있다.

Submission Name이 있으면 대체로 unreviewed protein 으로 보인다. 다만, 없다고 하여 reviewed 된 것은 아니더라



이름이 없는 protein은 Search할 당시에 사용했던 FASTA가 현재의 DB와 맞지 않아 생기는 Accession ID의 문제로 보인다. 이 부분은 고민해보겠다.

context






<br>

## 4. 이 문서의 향후 개선방향
- 개선점 1
- 개선점 2

<br>

## Reference
(1) 저자명 et al. 저널명 연도, 권(호):쪽수. doi:10.xxxx/xxxx.

(2)


[Ext1]:https://blog.naver.com/simhc0714