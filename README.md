# DL_HW
BME DeepLearning HomeWork

MIRA Team

**Check the following things to understand our work:**
  * Checkpoint 1:
    * HF.docx: The documentation of our work.
    * DATA/RAW/Measure_01/: Raw measurement files from IMU, MoCap and Robot
    * Code/data_loader.ipynb: You can find the data loading, visualization
  * Checkpoint 2:
    * DATA/RAW/Measure_02/: New improved measurement files from IMU and MoCap
    * Code/data_loader.ipynb: Load and visualize the new measurements
    * Code/MIRAnet_Test_01_MARK.ipynb: Our first 1Dconvnet solution for the problem, based on the code from practice. We tried to predict x and z coordinates here. The results are not perfect, but we see the potential.
  * Final Checkpont:
    * HF.pdf: The final documentation of our work.
    * Multiple measurements are found in the DATA/RAW library. We finally only used data from DATA/RAW/Measure_04. In this folder, you can find a separate README.txt file, which describes the content in the subfolders next to it.
    * Code\Bazs\README.txt file explainst the steps of data preprocessing and visualization.
    * Code\Bazs\1_DataLoad_and_Preprocess.ipynb notebook creates usable data from the raw datastream.
    * Code\Bazs\1_DataLoad_and_Preprocess.ipynb notebook contains our LSTM network. We did not manage to reach promising results in this direction.
    * Code\CNN_absolute.ipynb notebook contains our 1D CNN network for predicting absolute position and orientation values, which also did not performed quite well.
    * Code\CNN_relative.ipynb notebook contains our 1D CNN network for predicting relative values. This network produced the most promising results, but it is also not applicable yet, so further research work is needed.
