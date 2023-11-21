import time
import serial

def main():
    port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=None)
    while True:
        line = port.readline()     # 시리얼모니터 한 줄 ( ~~ 센서 인식값 : @@@ )
        arr = line.split()
        if len(arr) < 3:   # 인식값이 아니면..
            continue

        temp_data = ""

        dataType = arr[0]       # 온도 or 습도 or 가스
        data = float(arr[3])
        if dataType == '가스':
            temp_data += ("가스 인식값 : %.1f" % data)
        elif dataType == '온도':
            temp_data += ("온도 인식값 : %.1f" % data)
        elif dataType == '습도':
            temp_data += ("습도 인식값 : %.1f" % data)       # 센서 구별 -> 보내기  더 좋은 방법 찾아보기

        time.sleep(0.01)

# main() 부분 코드를 라즈베리파이 > 서버 통신 코드에 합칠 수 있으면 좋을 듯


if __name__ == "__main__":
    main()
