import sys
import time
import numpy as py
import cv2
from matplotlib import pyplot as plt

numbers = [5, 10, 25, 50, 100, 200]

for n in numbers:

    index = 1;
    while(index < 21):

        # Parametros
        txtv = "{0}".format(index);
        txtn= "{0}".format(n);
        I = cv2.imread("BasePicture.jpg", 0);
        V = cv2.VideoCapture("BaseVideo.mp4");
        # Criação do ORB
        orb = cv2.ORB_create(nfeatures = n);
        # Cria os algoritmos de matching
        BFM_Hamming = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = False);
        BFM_Euclidian = cv2.BFMatcher(cv2.NORM_L2, crossCheck = False);

        KNN_Hamming = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = False);
        KNN_Euclidian = cv2.BFMatcher(cv2.NORM_L2, crossCheck = False);

        FLANN_INDEX_KDTREE = 0;
        FLANN_INDEX_PARAMS = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5);
        FLANN_SEARCH_PARAMS = dict(checks=50);
        FLANN = cv2.FlannBasedMatcher(FLANN_INDEX_PARAMS,FLANN_SEARCH_PARAMS);
        # Obtem Id
        Ik, Id = orb.detectAndCompute(I, None);
        # Abre os arquivos de medição de tempo
        measure_BFM_HAMMING = open("MEASURE_BFM_HAMMING_N" +txtn + "_A" + txtv + ".txt", "w");
        measure_BFM_EUCLIDIAN = open("MEASURE_BFM_EUCLIDIAN_N" +txtn + "_A" + txtv + ".txt", "w");

        measure_KNN_HAMMING = open("MEASURE_KNN_HAMMING_N" +txtn + "_A" + txtv + ".txt", "w");
        measure_KNN_EUCLIDIAN = open("MEASURE_KNN_EUCLIDIAN_N" +txtn + "_A" + txtv + ".txt", "w");

        measure_FLANN = open("MEASURE_FLANN_N" +txtn + "_A" + txtv + ".txt", "w");

        if(not V.isOpened()):
            print("Problems to read the video ...");
            sys.exit();

        while(1):
            ret, frame = V.read();

            if(ret):
                F = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

                Fk, Fd = orb.detectAndCompute(F, None);

                BFMH_startTime = time.clock();
                matches = BFM_Hamming.match(Id, Fd);
                matches = sorted(matches, key = lambda x:x.distance);
                BFMH_elapsedTime = time.clock() - BFMH_startTime;
                measure_BFM_HAMMING.write("%.20f\n" % BFMH_elapsedTime);

                BFME_startTime = time.clock();
                matches = BFM_Euclidian.match(Id, Fd);
                matches = sorted(matches, key = lambda x:x.distance);
                BFME_elapsedTime = time.clock() - BFME_startTime;
                measure_BFM_EUCLIDIAN.write("%.20f\n" % BFME_elapsedTime);

                KNNH_startTime = time.clock();
                matches = KNN_Hamming.knnMatch(Id, Fd, k=3)
                KNNH_Good = [];
                for m,n in matches:
                    if m.distance < 0.75*n.distance:
                        KNNH_Good.append([m]);
                KNNH_elapsedTime = time.clock() - KNNH_startTime;
                measure_KNN_HAMMING.write("%.20f\n" % KNNH_elapsedTime);
                
                KNNE_startTime = time.clock();
                matches = KNN_Euclidian.knnMatch(Id, Fd, k=3)
                KNNE_Good = [];
                for m,n in matches:
                    if m.distance < 0.75*n.distance:
                        KNNE_Good.append([m]);
                KNNE_elaspedTime = time.clock() - KNNE_startTime;
                measure_KNN_EUCLIDIAN.write("%.20f\n" % KNNE_elaspedTime);

                FLANN_startTime = time.clock();
                matches = FLANN.knnMatch(Id,Fd,k=3);
                FLANN_elapsedTime = time.clock() - FLANN_startTime;
                measure_FLANN.write("%.20f\n" % FLANN_elapsedTime);

                cv2.imshow("", F);
            else:
                break;
            
            key = cv2.waitKey(30) & 0xFF;
                
            if((key==27)|(key==141)|(not ret)): 
                break;

        measure_BFM_HAMMING.close();
        measure_BFM_EUCLIDIAN.close();
        measure_KNN_HAMMING.close();
        measure_KNN_EUCLIDIAN.close();
        measure_FLANN.close();
        cv2.destroyAllWindows();

        index += 1;
    
sys.exit();
