
# 1. 실행되기 위한 조건
파일 확인
```
1 - 입찰운영사업팀.py <- 실행 파일
2 - extractors.worldMemory.py <- exextractors 라는 폴더 안에 worldMemory.py 
3 - extractors.nanoMemory.py <- exextractors 라는 폴더 안에 nanoMemory.py 
4 - extractors.danawa.py <- exextractors 라는 폴더 안에 danawa.py 
5 - file.py
```

모듈 설치
```
pip install selenium openpyxl python-dateutil beautifulsoup4 pandas requests
```

# 2. 파일 설명

### 입찰운영사업팀.py
```
- 실행 파일
```
### worldMemory.py
```
- 월드메모리 사이트 크롤링 및 리스트 데이터 저장
```
### nanoMemory.py
```
- 나노메모리 사이트 크롤링 및 리스트 데이터 저장
```
### danawa.py
```
- 다나와 사이트 크롤링 및 리스트 데이터 저장
```
### file.py
```
- 크롤링한 데이터를 csv 파일로 저장
```

# 3. 이력
## 2023.02.12
비딩 사업 데이터 크롤링 자동화 프로세스(완전자동화 목표)
- 3개 사이트 데이터 크롤링
- 크롤링 데이터 "it_data.xlsx"에 업데이트 

## 2023.04.10
방식 변경
- 3개 사이트 데이터 크롤링
- 크롤링 데이터 "{오늘 날짜}.csv" 파일로 저장
- 저장한 파일을 담당자가 확인 및 복사하여 데이터 취합 파일에 저장

## 2023.04.26(수)
- 불필요한 파일 삭제 및 정리

# 4. 추후에 예상되는 오류
- 사이트 구조 변경 또는 기존에 팔던 제품을 더 이상 팔지 않는 경우 오류 발생 가능성 有