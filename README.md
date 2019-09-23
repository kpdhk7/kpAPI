# kpAPI
Framework: Python/Django
Strategy for solve webserver:
- 장고의 모델에 csv에 존재하는 최소한의 필드를 만들고, django-rest-framework 를 이용해 CRUD스러운 동작을 할 수 있음과 동시에 pandas dataframe을 사용할 수 있는 기반을 만들어둔다
- 현재의 문제는 단순히 장비에 따른 이용률이었기에 엄청나게 큰 csv에 대한 chunk 분할 대응을 고려하지 않았고, 따라서 pandas의 dataframe 기반으로 저장을 수월하게 처리했다. 그러나 상황과 조건이 달라진다면 다른 형태로 대응해야 할 것이다.
- api내에서 장비간의 이용률을 비교한다던가 수년간의 최고 장비 이용률을 계산하는 것에 있어 현재는 데이터가 그렇게 많지 않기에 django object filter기능으로 대부분을 처리하였다. 그러나 더 큰 데이터베이스 규모를 상정한다면 다른 형태로 처리해야 할 것이다.
Build:
- 현재는 수월한 unittest를 위해 master 브랜치에 권한기능을 삭제한 상태이다. 하지만 postman으로 해당 웹서버를 테스트한다고 가정하고 이미 구현한 JWT Token기능을 사용한다는 전제하에 이 저장소를 빌드하고 실행하고 테스트하는 법을 기술하겠다.
- 1. python 환경 구성
- 기본적인 python, pip 및 가상환경은 설치되어있다고 가정하고 소스폴더 내에서 'pip install requirements.txt'로 구동에 필요한 라이브러리를 설치한다.
- 'python manage.py makemigrations', 'python manage.py migrate'로 장고가 기본적으로 쓰는 sqlite local db를 설정한다.
- 2. django webserver 구동
- 'python manage.py runserver' 로 localhost중심의 django를 구동할 수 있다. 이걸 구동시킨 상태에서 postman으로 테스트를 할 수 있다.
- 3. postman test
- a) token 발급:
- POST: 'http://localhost:8000/api/token/', Body에서 form-data형식으로 username:kakaotest, password:kakao 로 kv설정하면 response로 token을 받을 수 있다.
- 'api/token/verify'로 해당 토큰 유효성검사를 할 수 있고, 'api/token/refresh'로 새로운 토큰을 발급받을 수 있다.
- b) api test:
- 발급받은 JSON token을 Header탭에 Key: 'Authorization' 으로 넣고 Value: 'JWT {token_Value}' 형식으로 넣으면 API인증기능에 jwt token을 사용할 수 있다.
- 각 api는 다음과 같다.
- 1)데이터 파일 저장 : GET 'http://localhost:8000/api/read/'
- 2)접속 기기 목록을 출력: GET 'http://localhost:8000/api/devices/'
- 3)각 년도별 가장 많이 이용하는 접속기기: GET 'http://localhost:8000/api/mostallyears/'
- 4)특정 년도 가장 많이 이용하는 접속기기: POST 'http://localhost:8000/api/mostinyear/' Body;form-data{year:2017}
- 5)디바이스 접속 비율이 가장 많은 해: POST 'http://localhost:8000/api/mostindevice/' Body;form-data{device_id:DIS7864654}
