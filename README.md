# 👑 무선네트워크 프로젝트 2조
## 👩‍👩‍👦 조원 : 안재민(jaemin-i), 신지성(jssdre), 강교진(gyojinnK), 김인기(ikk5515), 최지혁(choiji12), 조광연(ebcsrh)
<hr/>

# 📡 프로젝트 주제
 - 여러가지 측정센서(ex 연기가스, 온습도, 불꽃감지 등)들에 대한 웹 API 플랫폼 제작
   > 여러가지 센서를 연결해서 원하는 센서의 데이터를 요청받는 API 플랫폼 <b>(범용성이 좋은 미들웨어)</b>
 
   ~~여러가지 측정 센서(연기가스, 온습도, 불꽃감지 등)이용 웹 API 제작~~ 
   ~~> 어떤 센서를 이용하더라도 API 통신으로 값을 호출할 수 있도록~~

# 🔖 산출물
 - 라즈베리파이와 아두이노를 이용한 각종 센서 값을 호출하는 API 사이트

# 📃 구현 계획
 - 최소 기능
   - 특정 센서(최소 2개 이상)의 데이터 값을 API 호출로 값 받아오기
 - 추가 기능
   - 연결된 센서의 데이터 값을 LED를 이용해서 시각화

# 🛠️ 주요 기술 및 장치
 - 아두이노
 - 라즈베리파이
 - 가스센서 or 미세먼지 센서
 - MQ2 연기가스감지 센서
 - DHT-11 온습도 센서
 - 불꽃감지 센서 

# ⚠️ 초기 유의사항
 - 장비의 유무
   - 프로젝트 진행에 있어 <b>주요 장비</b>가 구비 되어있는지

# 👩🏻‍💻 역할분담
 - 조광연: 아두이노를 프로그래밍하여 센서에 값을 읽어오는 작업 수행 및 라즈베리파이에 값 전달
 - 강교진, 김인기: 아두이노로 부터 전달받은 데이터를 처리하고, 그 데이터를 서버로 전송하는 프로그램
 - 안재민, 신지성: 서버 구축, 라즈베리파이로부터 받은 데이터를 API 형태로 제공
 - 최지혁: 사용자가 API를 통해 데이터를 쉽게 볼 수 있는 웹 또는 앱 개발

# 🏗️ 시스템 아키텍처
각 단계별 사용 장치 및 스택
> 지속적인 업데이트 예정
 - 센서 단계: 아두이노와 라즈베리파이에 연결된 센서들, 아두이노로 데이터 전송
 - 하드웨어 단계: 아두이노/라즈베리파이. 센서 데이터를 수신, 처리 후 서버에 전송
 - 서버 단계: 센서 데이터를 수신, 처리 및 저장하고 API를 통해 데이터를 클라이언트에 제공
 - 클라이언트 단계: 사용자가 접근하는 웹 서비스. API를 통해 서버로부터 수신한 데이터를 사용자에게 제공

[시스템 아키텍처](https://github.com/inhatc-RPi/project/assets/97776614/6d4d0a44-cc4d-4861-b40e-e0edcae7d953)
![시스템아키텍처](https://github.com/inhatc-RPi/project/assets/97776614/6d4d0a44-cc4d-4861-b40e-e0edcae7d953)

# 진행사항
<h3>2023.11.12 ~ 2023.11.19</h3>
 <ol>
  <h3>api 설계</h3>
  <li>
   <p>구조</p>
    <img width="1406" alt="스크린샷 2023-11-20 오후 9 45 58" src="https://github.com/inhatc-RPi/project/assets/113239209/3a56a991-b00a-47bd-97b2-47c2425479a9">
   </li>
  <li>
   <p>/view/{sensor}</p>
    <img width="834" alt="스크린샷 2023-11-21 오전 12 05 41" src="https://github.com/inhatc-RPi/project/assets/113239209/5e1fbf30-734c-4133-90d8-9d3e2a14b770">
   </li>
  <li>
   <p>/change/</p>
    <img width="828" alt="스크린샷 2023-11-20 오후 9 44 32" src="https://github.com/inhatc-RPi/project/assets/113239209/7a7b0f5c-9b97-421d-871a-6395c02e2028">
   </li>
</ol> 
<br><br><br>
    
<h3>2023.11.20 ~ 2023.11.27</h3>
 <ol>
  <li>
  <h3>cloudtype을 이용한 백엔드 배포</h3>
  <img width="1186" alt="스크린샷 2023-11-27 오후 11 43 06" src="https://github.com/inhatc-RPi/project/assets/22267184/fc12d31c-b572-47f5-9104-3399d4d918e4">
  </li>
  <li>
   <h3>라즈베리파이 데이터 송수신 구현</h3>
   
   ![무선넷_시스템_아키텍처의 사본](https://github.com/inhatc-RPi/project/assets/97776614/9e233a1f-6234-4332-9016-b6cef2b0379d)
   
  </li>
 </ol>
   

# #️ 참조
 - 교수님GitHub: [2023_inhatc](https://github.com/sonnonet/2023_inhatc)
 - 세미넷: [라즈베리파이를 이용한 화재 및 가스 누출 경보기](https://www.seminet.co.kr/channel_micro.html?menu=video_sub&com_no=918&video_id=7498&cate_no=44&cate_name=Raspberry+pi)
 - DBpia: [라즈베리파이와 가스센서를 이용한 화재 및 가스누출 감지기 개발](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07467666)
 - vue_api: [vue와 api연동](https://jeong-dev-blog.tistory.com/4)







 
