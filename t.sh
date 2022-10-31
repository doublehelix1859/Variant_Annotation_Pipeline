#Stage2
#bsub -J STEP1 < STEP1.lsf
bsub -J STEP2 < STEP2.lsf

#Stage3
bsub -J STEP3 -w 'done(STEP2)' < STEP3.lsf

#Stage4
bsub -J STEP4_1 -w 'done(STEP3)' < STEP4_1.lsf
bsub -J STEP4_2 -w 'done(STEP3)' < STEP4_2.lsf
bsub -J STEP4_3 -w 'done(STEP4_2)' < STEP4_3.lsf
bsub -J STEP4_4 -w 'done(STEP4_3)' < STEP4_4.lsf

#Stage5
#Step5_2 is manually done

#Stage6
bsub -J STEP5 -w 'done(STEP4_1)' < STEP5.lsf
bsub -J STEP6 -w 'done(STEP5)' < STEP6.lsf
bsub -J STEP7 -w 'done(STEP6)' < STEP7.lsf
bsub -J STEP8 -w 'done(STEP7)' < STEP8.lsf

#Stage7
bsub -J STEP9 -w 'done(STEP8)' < STEP9.lsf
bsub -J STEP10 -w 'done(STEP9)' < STEP10.lsf

#Stage8
bsub -J STEP11 -w 'done(STEP10)' < STEP11.lsf

#Stage10
bsub -J STEP12 -w 'done(STEP11)' < STEP12.lsf

#Stage11
bsub -J STEP13 -w 'done(STEP12)' < STEP13.lsf

#Stage12
bsub -J STEP14 -w 'done(STEP13)' < STEP14.lsf

#Stage13
bsub -J STEP15 -w 'done(STEP14)' < STEP15.lsf
bsub -J STEP16 -w 'done(STEP15)' < STEP16.lsf

