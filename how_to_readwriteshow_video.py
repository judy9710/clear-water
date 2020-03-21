import cv2



cap = cv2.VideoCapture(0)



fourcc = cv2.VideoWriter_fourcc(*'XVID')

# fourcc 라는 것은 4 글자 코드라는 뜻이며 4바이트로 된 문자열은 데이터 형식을 구분하는 고유 글자가 된다. 주로 avi 파일의 영상 코덱을 구분할 때 사용된다. 'DIVX', 'XVID' 등이 많이 사용되는 확장자이다. 

# 우선 'XVID' 확장자로 fourcc 인스턴스를 만들어주고



out = cv2. VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# VideoWriter의 첫번째 인자는 write 할 파일명- 'output.avi'

# 두번째 인자로 fourcc 즉 확장자명을 전달하고

# 세번째 인자는 1초에 이용할 프레임 수, 즉 20개

# 프레임(비디오)의 크기

# out 인스턴스 생성 완료



while (True):

    ret, frame = cap.read()  
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv2.imshow('frame', frame) 

        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break

        else:
            break



cap.release() 

cv2.destroyAllWindows()  
