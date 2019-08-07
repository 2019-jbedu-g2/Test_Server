# Server 구동


> 서버 구동시 첫 설정.  git에서 처음 한번만 받을 때 이 과정을 따를 것.

 . 파이참 실행 
 
 . create new project/open/check out from version control 메뉴 중에서 check out from version control 선택
 
 . 만약 이전에 실행된 적이 있어 프로젝트가 바로 실행이 되면 file-close project 하여 처음 화면으로 돌아감.
 
 . git 선택하여 clone repository 창이 뜨면 git로그인 
 
 . URL 에서 Test-server.git 선택하고 옆에 Test버튼 클릭
 
 . Directory는 적절하게 생성바람.
 
 . VCS-Git-branches-origin/django-server-rebase current onto selected
 
 . 실행할 때마다 git로그인이 귀찮으면 File-settings-version control-github-add(+)
 
 . 가상환경 만들기
 
 . 파이참 창아래 python console/terminal/todo 기타등등 terminal선택
 
 . cd store / python -m venv venv 입력
 
 . 왼쪽 트리에서 venv폴더가 생성된 걸 확인가능
 
> 인터프리터 설정과 장고, 오라클 라이브러리, rest-framework 설치
 
 . File-settings-project:XXXXXX-project Interpreter-project Interpreter입력창 옆에 설정버튼 클릭- add클릭-ok클릭
 
 . Latest version옆에 +클릭하여 검색 창에 django 입력 version 2.2.3버전(2019/7/18일자) 확인 후 install package 클릭
 
 . 설치 후 cx-Oracle 검색 후 version 7.2.0 확인 후 install package 클릭
 
 . 설치 후 django-rest-framework 검색 후 version 0.1.0 확인후 install package클릭
 
 . 설치 후 pywin32검색 후 install package 선택
 
 . 설치 후 Channels 검색 후 install package 선택
 
 . 설치 후 Channels-redis 검색 후 install package 
 
 . 창 닫고 apply - ok 후 창 닫기
 
 . 혹시 different sdk name 발생시 project interpreter입력창에서 show all 클릭 목록창 다 지우고 add(+)
 
 . Existing environment선택 후 ... 클릭하여 경로지정해줌. venv\Scripts\python.exe
 
 . terminal에서 cd venv 입력 / cd Scripts 입력 / activate 입력하여 가상환경 진입 프롬프트가 (venv)현재경로 > 이렇게 바뀜
 
 . 다시 terminal에서 cd.. / cd.. /cd store 입력 후 
 
 > DB구축 / DB와 서버 동기화 / Redis backend서버 설치
 
 . oracle express 18c에 데이터 베이스 파일 구축.
 
 . terminal 에서 py manage.py migrate 를 입력.
 
 . 완료 후 terminal 에서 py manage.py createsuperuser를 입력하여 아이디 admin, email 공란서 엔터, 암호 admin1234 입력하고 암호가 너무 평범하다 하면 y를 입력하여 슈퍼유저를 등록.
	 
 . https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504 에 들어가 Redis-x64-3.0.504.msi를 다운로드 받아 설치.
 
 . c:\program files\redis에 있는 redis.windows.conf파일을 메모장으로 열기.
 
 . 60번째 줄 # bind 127.0.0.1 을 #을 제거하여 주석을 해제하고 뒤에 8000을 붙여주고 저장.
 
 . redis-server.exe를 실행하여 cmd창이 사라지지 않고 케잌 모양이 뜨게 되면 성공.
 
   (만약 그렇지 않고 떳다 꺼지면 작업관리자를 열어 프로세스 란에서 redis-server를 찾아 프로세스 끝내기를 선택하여 끄고 설정파일을 다시 수정 한 뒤 꺼지지 않을 때 까지 다시 시도.)
   
# 서버 실행
	 
 . terminal 내 (venv) (설치된 경로)\store 상태에서
 
 . python manage.py runserver 0:8000 입력 /서버 작동.
 
 . http://127.0.0.1:8000/store 입력하면 브라우저에서 확인가능.
 
# redis 서버란?

 . django 서버는 웹서버로 일반적인 http 서버로 작동하지만, channels 업데이트 이후 channels를 통해 웹 소켓 통신이 가능하게 되었다.
 
 . 하지만 웹 소켓 연결 시 서버와의 연결은 되지만 각 클라이언트끼리는 연결되어 있지 않은데 channels layer를 통해 연결이 가능하다.
 
 . 그러기 위해선 backend에서 클라이언트간에 연결을 할 수 있도록 지원이 필요한데 이번 프로젝트에선 수많은 기능들 중 redis를 통해 연결하였다.
 
 . redis는 windows를 지원하지 않고 리눅스 기반이나 위의 깃 허브를 통해 윈도우즈 버전으로 포팅한 redis를 사용 할 수 있다. 
 

# URL 요청 내역

 > http://192.168.0.(본인 컴퓨터ip끝자리):8000 이후 해당 url을 넣도록 한다.
 > http 통신 이며 웹소켓의 경우엔 ws://를 쓰도록 한다.

 . 가게전체정보 : /store/
 
 . 가게단일장보 : /store/가게번호
 
 . 줄서기	: /waiting/가게번호
 
 . 미루기	: /waiting/가게번호/본인바코드
 
 . 현재순서확인	: /waiting/confirm/가게번호/본인바코드	//우선 http요청으로 처리가능.
 
 . 오프줄서기	: /account/off/가게번호
 
 . 확인		: /account/confirm/본인바코드
 
 . 취소		: /account/cancel/본인바코드
 
 . 매장앱 로그인 : account/login/가게아이디/가게비밀번호


