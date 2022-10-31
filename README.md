# Variant_annotation_pipeline
Gene annotation combining Ensembl Variant Effect Predictor (VEP) and other external databases

Purpose
1. To identify disease-causing mutations, genes, and pathway in larger scale NGS data
2. To identify other functional elements


# An Overview of the pipeline #

<img width="925" alt="Screen Shot 2022-10-31 at 3 45 55 PM" src="https://user-images.githubusercontent.com/24422230/199097132-c4d9e8ff-3ca6-4b0b-85ae-68473596ea35.png">

Fig 1. The workflow of VEP annotation pipeline (from Stage 0 to Stage M)
          The flowchart above represents the workflow applied to the vcf containing more than 100,000 variants. Stage 0 performs the roles of vcf split, its processing and preparing initiator which initiates the downstream stages: 1 ~ 7 and Post(P). After completing these stages, STEP M should be taken to concatenate all the results obtained from Stage P.

<img width="1310" alt="Screen Shot 2022-10-31 at 3 34 27 PM" src="https://user-images.githubusercontent.com/24422230/199095386-010ae2ed-d923-4ecf-8818-1918e292af79.png">

Fig 2. The workflow of VEP annotation pipeline (from Stage 1 to Stage 7)
           Each STEP belonging to the stages must be executed sequentially except the total of 4 STEPs in Stage 2. Those STEPs can be executed   
           simultaneously because all of them require the output from STEP3 as the inputs. Also, Stage 4 which contains STEP BM is not necessarily 
           included in the pipeline. The output from that stage has already been prepared in sources. Thus, a user can use the ready-made output as the 
           input of the next stage: Stage 5.


(the detailed stepwise work is included in the manual: VEP annotation pipeline Manual.docx.pdf)
