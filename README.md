# Working Commands


- ## Command to run inference using infer.py

- ### Example: Running inference on the whole kitti dataset (from sequences 00 to 21), using pretrained model darknet 21 which is saved in the directory darknet21, give the predictions directory for saving the predictions.

```
$ ./infer.py -d /work/akmt/data/dataset -l /work/akmt/lidar-bonnetal/train/tasks/semantic/pretrained_model_predictions -m /work/akmt/lidar-bonnetal/train/tasks/semantic/pretrained_models/darknet21 
```

- ## For Ground Truth Visualization of sequence 00 in the sematics kitti dataset:


```
$ ./visualize.py -d /work/akmt/data/dataset -s 00
```

- ## For  Model's Predictions Visualization for Sequence 00
 
 ```
 ./visualize.py -p /work/akmt/lidar-bonnetal/train/tasks/semantic/pretrained_model_predictions/darknet21 -d /work/akmt/data/dataset -s 00
 ```

 - ## For Calculating IoU of the Point Clouds on the validation split (Sequence 08)
 ```
 ./evaluate_iou.py -p /work/akmt/lidar-bonnetal/train/tasks/semantic/pretrained_model_predictions/darknet21  -d /work/akmt/data/dataset --split valid
 ```
- ## IoU results of the Darkent21 == RangeNet21 on the validation set al
 ```
 Validation set:
Acc avg 0.882
IoU avg 0.472
IoU class 1 [car] = 0.842
IoU class 2 [bicycle] = 0.242
IoU class 3 [motorcycle] = 0.345
IoU class 4 [truck] = 0.310
IoU class 5 [other-vehicle] = 0.202
IoU class 6 [person] = 0.354
IoU class 7 [bicyclist] = 0.456
IoU class 8 [motorcyclist] = 0.000
IoU class 9 [road] = 0.934
IoU class 10 [parking] = 0.432
IoU class 11 [sidewalk] = 0.806
IoU class 12 [other-ground] = 0.001
IoU class 13 [building] = 0.790
IoU class 14 [fence] = 0.479
IoU class 15 [vegetation] = 0.817
IoU class 16 [trunk] = 0.488
IoU class 17 [terrain] = 0.716
IoU class 18 [pole] = 0.393
IoU class 19 [traffic-sign] = 0.353
 ```


```
Results I get with pretrained weights (on validation split 08) :
0.842,0.242,0.345,0.310,0.202,0.354,0.456,0.000,0.934,0.432,0.806,0.001,0.790,0.479,0.817,0.488,0.716,0.393,0.353,0.472
Results in the Paper on test set (11-21):
85.4 26.2 26.5 18.6 15.6 31.8 33.6 4.0 91.4 57.0 74.0 26.4 81.9 52.3 77.6 48.4 63.6 36.0 50.0 47.4
```

- ## Warning before training:
```
/home/abhishek/anaconda3/envs/bonnetal2/lib/python3.7/site-packages/torch/nn/parallel/_functions.py:61: UserWarning: Was asked to gather along dimension 0, but all input tensors were scalars; will instead unsqueeze and return a vector.
  warnings.warn('Was asked to gather along dimension 0, but all '
Lr: 0.000e+00 | Update: 7.677e+00 mean,2.693e+01 std | Epoch: [0][0/2270] | Time 1048.951 (1048.951) | Data 1.600 (1.600) | Loss 2.9784 (2.9784) | acc 0.025 (0.025) | IoU 0.009 (0.009)
../../tasks/semantic/modules/trainer.py:354: RuntimeWarning: invalid value encountered in float_scalars
  update_ratios.append(update / max(w, 1e-10))
```