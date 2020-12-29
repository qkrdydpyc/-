#2019-06-11
import os
import numpy
import shutil
"""
* 파일: preprocessing.py
* 기능
  1. 데이터셋을 읽어 들여 운전자, Trip 별 특정 feature 로 구성된 데이터를 생성(./normal)
  2. ./normal 의 데이터를 기준으로 sliding window 를 적용하여 3개의 통계적인 데이터 생성(./mean, ./median, ./std)

* 전역변수
  1. header: 데이터셋에서 첫번째 행에 해당되는 feature 의 name 이 들어가는 리스트
  2. Driver_data: 실제 주행 데이터의 값이 들어가는 리스트
  3. useful_data: 전체 feature 중 전처리할 feature 의 인덱스가 들어간 리스트
  4. a_q: 사용할 feature 들의 실제 데이터가 들어가는 리스트
  5. A ~ I 이중 리스트: 운전자별로 구분된 데이터가 들어가는 리스트

* 함수
  1. readfile(): 데이터셋(.csv)을 읽어 운전자와 주행 라운드 수 를 분류하여 A ~ I의 리스트에 저장
  2. writefile(result_path): A ~ I 리스트에 있는 데이터에 대해서 각각 "운전자_주행라운드 수.csv"의 이름의 데이터 write (./normal)
  3. normal_read(num, alphabet): 2의 과정에서 생성된 파일들을 read 하여 a_q 리스트에 저장
  4. mean_write(window_size): a_q 리스트에 들어있는 데이터에 대하여 sliding window를 적용하여 평균으로 데이터를 write (./mean)
  5. median_write(window_size): a_q 리스트에 들어있는 데이터에 대하여 sliding window를 적용하여 중간값으로 데이터를 write (./median)
  6. std_write(window_size): a_q 리스트에 들어있는 데이터에 대하여 sliding window를 적용하여 표준편차로 데이터를 write (./std)
  7. total_wrtie(window_size): a_q 리스트에 들어있는 데이터에 대하여 sliding window를 적용하여 평균, 중간값, 표준편차의 모든 데이터를 write (./total)
"""
header=[]
a_q = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
Driver_data = []
useful_data = [11, 4, 1, 0, 14, 22, 19, 20, 31, 17, 34, 35, 37, 38, 32, 53]
A = [[], [], [],[], [], [],[], [], []]
B = [[], [], [],[], [], [],[], [], []]
C = [[], [], [],[], [], [],[], [], []]
D = [[], [], [],[], [], [],[], [], []]
E = [[], [], [],[], [], [],[], [], []]
F = [[], [], [],[], [], [],[], [], []]
G = [[], [], [],[], [], [],[], [], []]
H = [[], [], [],[], [], [],[], [], []]
I = [[], [], [],[], [], [],[], [], []]



#데이터셋 읽어오기
def readfile():
    with open('1st KU-Driving Dataset final - City relase.csv') as f: #일반 파일 읽어오기
        line_counter = 0
        while 1:
            data = f.readline()
            if not data:
                break
            if line_counter == 0:
                header2 = data.split(",")
                header3 = []
                for j in useful_data: # 주요 Feature 만 분류
                    header3.append(header2[j])
                header.append(header3)# Feature 저장
            else:
                Driver_data = data.split(",")
                if Driver_data[53][0] == "A":                       #사용자 별 분류
                    A[int(Driver_data[51]) - 1].append(Driver_data) #주행구간 별 분
                elif Driver_data[53][0] == "B":
                    B[int(Driver_data[51]) - 1].append(Driver_data)
                elif Driver_data[53][0] == "C":
                    C[ int(Driver_data[51]) - 1].append(Driver_data)
                elif Driver_data[53][0] == "D":
                    D[int(Driver_data[51]) - 1].append(Driver_data)
                elif Driver_data[53][0] == "E":
                    E[int(Driver_data[51]) - 1].append(Driver_data)
                elif Driver_data[53][0] == "F":
                    F[int(Driver_data[51]) - 1].append(Driver_data)
                elif Driver_data[53][0] == "G":
                    G[int(Driver_data[51]) - 1].append(Driver_data)
                elif Driver_data[53][0] == "H":
                    H[int(Driver_data[51]) - 1].append(Driver_data)
                elif Driver_data[53][0] == "I":
                    I[int(Driver_data[51]) - 1].append(Driver_data)
            line_counter += 1;


#사용자, 주행구간 별로 분류 후 'normal'하위에 저장
def writefile(result_path):
    for i in range(0,9):
        if len(A[i]) > 0: #사용자 A에 대한 데이터가 앞서 읽어온 파일에 존재할 경우 if 문 실행
            with open(result_path+'A_'+str(i)+'.csv', 'w') as f: #사용자 'A'의 주행구간 'i'에서의 주행 데이터를 저장할 파일 생성 또는 열기
                for Driver_data in A[i]:
                    Driver_data2 = []
                    for j in useful_data:
                        Driver_data2.append(Driver_data[j])
                    Driver_data2[len(Driver_data2)-1]='1\n'
                    f.write(",".join(Driver_data2)) #파일에 사용자의 주행 데이터 저장
    for i in range(0,9):
        if len(B[i]) > 0:
            with open(result_path+'B_'+str(i)+'.csv', 'w') as f:
                #f.write(",".join(header[0]))
                for Driver_data in B[i]:
                    Driver_data2 = []
                    for j in useful_data:
                        Driver_data2.append(Driver_data[j])
                    Driver_data2[len(Driver_data2) - 1] = '1\n'
                    f.write(",".join(Driver_data2))
    for i in range(0,9):
        if len(C[i]) > 0:
            with open(result_path+'C_'+str(i)+'.csv', 'w') as f:
                #f.write(",".join(header[0]))
                for Driver_data in C[i]:
                    Driver_data2 = []
                    for j in useful_data:
                        Driver_data2.append(Driver_data[j])
                    Driver_data2[len(Driver_data2) - 1] = '1\n'
                    f.write(",".join(Driver_data2))
    for i in range(0,9):
        if len(D[i]) > 0:
            with open(result_path+'D_'+str(i)+'.csv', 'w') as f:
                #f.write(",".join(header[0]))
                for Driver_data in D[i]:
                    Driver_data2 = []
                    for j in useful_data:
                        Driver_data2.append(Driver_data[j])
                    Driver_data2[len(Driver_data2) - 1] = '1\n'
                    f.write(",".join(Driver_data2))
    for i in range(0,9):
        if len(E[i]) > 0:
            with open(result_path+'E_'+str(i)+'.csv', 'w') as f:
                #f.write(",".join(header[0]))
                for Driver_data in E[i]:
                    Driver_data2 = []
                    for j in useful_data:
                        Driver_data2.append(Driver_data[j])
                    Driver_data2[len(Driver_data2) - 1] = '0\n'
                    f.write(",".join(Driver_data2))


#aplhabet 에 해당하는 운전자('A','B'...)의 num에 해당하는 주행구간(1,2,..) 데이터 읽어오기
def normal_read(num, alphabet):
    if os.path.isfile('./normal/'+alphabet+'_'+str(num)+'.csv'):
        with open('./normal/' + alphabet + '_' + str(num) + '.csv') as file: #사용자, 주행구간 별로 분류 완료한 데이터 읽어오기
            line_counter = 1
            line = []
            data = file.readlines()
            for one_line in data:
                line.append(one_line)
                for i in range(0, len(a_q), 1):
                    if i <= 14:
                        a_q[i].append(float(line[line_counter - 1].split(",")[i]))
                    else:
                        a_q[i].append(line[line_counter - 1].split(",")[i])
                #파일을 한줄 단위로 읽어 들여 전역변수 'a_q'에 리스트 형태로 저장
                line_counter += 1

#평균값 통계 후 저장
def mean_write(window_size):
        with open('./mean/'+'mean.csv', 'a') as file: #통계값을 저장할 폴더 생성 또는 열기
            for z in range(0,len(a_q[0]),1):
                write_line=[]
                for i in range(0,len(a_q),1):
                    if i <= 14:
                        write_line.append(str(round(numpy.mean(a_q[i][z:z + window_size]) , 2)))
                        #numpy.mean함수를 사용하여 평균값 통계
                    else:
                        write_line.append(a_q[i][z])
                file.write(",".join(write_line))

def median_write(window_size):
    with open('./median/' + 'median.csv', 'a') as file:
        #file.write(",".join(header[0]))
        for z in range(0, len(a_q[0]), 1):
            write_line = []
            for i in range(0, len(a_q), 1):
                if i <= 14:
                    write_line.append(str(round(numpy.median(a_q[i][z:z + window_size]), 2)))
                else:
                    write_line.append(a_q[i][z])
            file.write(",".join(write_line))


def std_write(window_size):
    with open('./std/' +'std.csv', 'a') as file:
        #file.write(",".join(header[0]))
        for z in range(0, len(a_q[0]), 1):
            write_line = []
            for i in range(0, len(a_q), 1):
                if i <= 14:
                    write_line.append(str(round(numpy.std(a_q[i][z:z + window_size]), 2)))
                else:
                    write_line.append(a_q[i][z])
            file.write(",".join(write_line))


def total_write(window_size):
    with open('./total/' + 'total.csv', 'a') as file:
        # file.write(",".join(header[0]))
        for z in range(0, len(a_q[0]), 1):
            write_line = []
            for i in range(0, len(a_q), 1):
                if i <= 14:
                    write_line.append(str(round(numpy.mean(a_q[i][z:z + window_size]), 2)))
                    write_line.append(str(round(numpy.median(a_q[i][z:z + window_size]), 2)))
                    write_line.append(str(round(numpy.std(a_q[i][z:z + window_size]), 2)))
                else:
                    write_line.append(a_q[i][z])
            file.write(",".join(write_line))

def main():

    if not(os.path.isdir('./normal')):
        os.makedirs('./normal')
    else:
        shutil.rmtree('./normal')
        os.makedirs('./normal')
    if not(os.path.isdir('./mean')):
        os.makedirs('./mean')
    else:
        shutil.rmtree('./mean')
        os.makedirs('./mean')
    if not(os.path.isdir('./median')):
        os.makedirs('./median')
    else:
        shutil.rmtree('./median')
        os.makedirs('./median')
    if not(os.path.isdir('./std')):
        os.makedirs('./std')
    else:
        shutil.rmtree('./std')
        os.makedirs('./std')
    if not (os.path.isdir('./total')):
        os.makedirs('./total')
    else:
        shutil.rmtree('./total')
        os.makedirs('./total')
    window_size = 40 #window size 설정

    readfile() #데이터셋 읽어오기
    writefile('./normal/') #사용자, 주행구간 별로 분류 후 'normal'하위에 저장
    num=[0,1] #주행구간
    alphabet=['A','B','C','D','E'] #사용자

    for y in num:
        for z in alphabet:
            normal_read(y, z) #사용자, 주행구간 별로 분류 완료한 데이터 읽어오기
            mean_write(window_size) #평균값 통계 후 저장
            median_write(window_size) #중간값 통계 후 저장
            std_write(window_size) #표준편차 통계 후 저장
            total_write(window_size) #3가지 통계 저장
            header.clear()
            for x in range(0, len(a_q), 1):
                a_q[x].clear()


if __name__ == '__main__':
    main()
