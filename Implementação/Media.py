import time

# Criacao das variaveis de processamento
timesMeasured = 20;
pointAmounts = [5, 10, 25, 50, 100, 200];
algorithms = ["BFM_HAMMING", "BFM_EUCLIDIAN", "KNN_HAMMING", "KNN_EUCLIDIAN", "FLANN"];

index = 0;

for algorithm in algorithms:
    for pointAmount in pointAmounts:
        index = 1;

        samples = [];
        
        while(index <= timesMeasured):
            filename = "MEASURE_" + algorithm + "_N" + ("{0}".format(pointAmount)) + "_A" + ("{0}".format(index)) + ".txt";

            sample = open(filename, "r");

            i = 0;
            for line in sample:
                convertedValue = float(line);
                
                if(index == 1):
                    samples.append(convertedValue);
                else:
                    samples[i] += convertedValue;
                i += 1;
            
            sample.close();
            index += 1;

        mediaFileName = "MEASURE_" + algorithm + "_N" + ("{0}".format(pointAmount)) + "_MEDIA.txt";
        mediaFile = open(mediaFileName,"w");
        
        for sample in samples:
            mediaFile.write("%.20f\n" % (sample / timesMeasured));
