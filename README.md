# OpenBaek-Crawling

### 실제 DB 반영 크롤링 파일

##### db_input_crawling.py

- 분류가 되있는 문제 데이터 DB에 반영

##### all_problem_crawling.py

- 분류가 되어있는 문제 데이터 DB에 반영



### API에 직접적으로 이용하는 크롤링 파일

##### user_nums.py

- user의 id를 입력했을 때 해당 user의 백준 정보를 긁어오는 소스



### 테스트 크롤링 파일

##### category_crawling.py

- 초반 기획 및 디자인을 위해 카테고리 개수 및, 크기 파악을 위한 크롤링 파일

##### category_update_crawling.py

- 전체 14000문제 DB반영 후, 분류가 되어있는 문제 데이터를 update를 이용해서 DB에 반영하려고 했으나 실패



### 실행 방법

1. db_setting.py 파일 생성해서 pymysql connection 설정

2. ```shell
   python all_problem_crawling.py
   ```

3. ```shell
   python db_input_crawling.py
   ```

> 1 > 2 > 3 순서를 반드시 지켜주어야 합니다.