import time

resultFile = open("MEASURE_N5.txt","w");

fileBfmEuclidian = open("MEASURE_BFM_EUCLIDIAN_N5_MEDIA.txt","r");
fileBfmHamming = open("MEASURE_BFM_HAMMING_N5_MEDIA.txt","r");
fileKnnEuclidian = open("MEASURE_KNN_EUCLIDIAN_N5_MEDIA.txt","r");
fileKnnHamming = open("MEASURE_KNN_HAMMING_N5_MEDIA.txt","r");
fileFlann = open("MEASURE_FLANN_N5_MEDIA.txt","r");

vectorBfmEuclidian = [];
vectorBfmHamming = [];
vectorKnnEuclidian = [];
vectorKnnHamming = [];
vectorFlann = [];

mediaBfmEuclidian = 0;
mediaBfmHamming = 0;
mediaKnnEuclidian = 0;
mediaKnnHamming = 0;
mediaFlann= 0;

for line in fileBfmEuclidian:
    convertedValue = float(line);
    mediaBfmEuclidian += convertedValue;
    vectorBfmEuclidian.append(convertedValue);

mediaBfmEuclidian = mediaBfmEuclidian / len(vectorBfmEuclidian);
resultFile.write("MediaBfmEuclidian: %.20f" % mediaBfmEuclidian);

for line in fileBfmHamming:
    convertedValue = float(line);
    mediaBfmHamming += convertedValue;
    vectorBfmHamming.append(convertedValue);

mediaBfmHamming = mediaBfmHamming / len(vectorBfmHamming);
resultFile.write("\nMediaBfmHamming: %.20f" % mediaBfmHamming);

for line in fileKnnEuclidian:
    convertedValue = float(line);
    mediaKnnEuclidian += convertedValue;
    vectorKnnEuclidian.append(convertedValue);

mediaKnnEuclidian = mediaKnnEuclidian / len(vectorKnnEuclidian);
resultFile.write("\nMediaKnnEuclidian: %.20f" % mediaKnnEuclidian);

for line in fileKnnHamming:
    convertedValue = float(line);
    mediaKnnHamming += convertedValue;
    vectorKnnHamming.append(convertedValue);

mediaKnnHamming = mediaKnnHamming / len(vectorKnnHamming);
resultFile.write("\nMediaKnnHamming: %.20f" % mediaKnnHamming);

for line in fileFlann:
    convertedValue = float(line);
    mediaFlann += convertedValue;
    vectorFlann.append(convertedValue);

mediaFlann = mediaFlann / len(vectorFlann);
resultFile.write("\nMediaFlann: %.20f" % mediaFlann);

mediaOfMedias = 0;
mediaOfMedias = (mediaBfmEuclidian + mediaBfmHamming + mediaKnnEuclidian + mediaKnnHamming + mediaFlann) / 5;
resultFile.write("\nMediaOfMedias: %.20f" % mediaOfMedias);

m = 5;
n = len(vectorBfmEuclidian);

sqt = 0;
sqd = 0;

for measure in vectorBfmEuclidian:
    sqd += (measure - mediaBfmEuclidian) ** 2;
    sqt += (measure - mediaOfMedias) ** 2;

for measure in vectorBfmHamming:
    sqd += (measure - mediaBfmHamming) ** 2;
    sqt += (measure - mediaOfMedias) ** 2;

for measure in vectorKnnEuclidian:
    sqd += (measure - mediaKnnEuclidian) ** 2;
    sqt += (measure - mediaOfMedias) ** 2;

for measure in vectorKnnHamming:
    sqd += (measure - mediaKnnHamming) ** 2;
    sqt += (measure - mediaOfMedias) ** 2;

for measure in vectorFlann:
    sqd += (measure - mediaFlann) ** 2;
    sqt += (measure - mediaOfMedias) ** 2;

resultFile.write("\nSQT: %.20f" % sqt);
sqt_gl = (m * n - 1);
resultFile.write("\nGraus de Liberdade: %.20f" % sqt_gl);

resultFile.write("\nSQD: %.20f" % sqd);
sqd_gl = (m * (n - 1));
resultFile.write("\nGraus de Liberdade: %.20f" % sqd_gl);

sqe = sqt - sqd;
sqe_gl = m - 1;
resultFile.write("\nSQE: %.20f" % sqe);
resultFile.write("\nGraus de Liberdade: %.20f" % sqe_gl);
