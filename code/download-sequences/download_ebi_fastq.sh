#!/bin/bash

# download_ebi_fastq.sh
#
# Download per-sample fastq files for any sample accessions that have not been downloaded 
#  (do not exist in current directory).
# All 97 studies in EMP Release 1 (in order by Qiita study number) will be downloaded; if
#  fewer studies are desired, change the first line of code.

for study_accession in ERP021896 ERP020023 ERP020508 ERP017166 ERP020507 ERP017221 ERP016412 ERP020884 ERP020022 ERP020510 \
                       ERP017438 ERP016395 ERP020539 ERP016468 ERP020590 ERP020021 ERP020587 ERP020560 ERP020589 ERP017176 \
                       ERP017220 ERP017174 ERP016405 ERP020591 ERP021691 ERP016416 ERP022167 ERP021699 ERP016495 ERP022245 \
                       ERP016748 ERP016749 ERP016752 ERP016540 ERP006348 ERP016543 ERP016746 ERP016586 ERP016735 ERP021864 \
                       ERP016588 ERP016587 ERP016539 ERP016734 ERP016492 ERP016592 ERP003782 ERP016607 ERP016581 ERP016557 \
                       ERP016464 ERP016542 ERP016541 ERP016591 ERP016854 ERP016852 ERP016286 ERP016451 ERP023684 ERP016869 \
                       ERP010098 ERP016879 ERP016883 ERP016466 ERP016496 ERP016880 ERP016455 ERP016900 ERP016924 ERP016923 \
                       ERP016925 ERP016927 ERP016469 ERP016329 ERP016926 ERP021540 ERP021541 ERP021542 ERP021543 ERP021544 \
                       ERP021545 ERP016937 ERP016131 ERP016483 ERP016252 ERP022166 ERP016414 ERP016472 ERP023686 ERP017459 \
                       ERP016287 ERP016285 ERP005806 ERP021895 ERP016384 ERP016491 ERP006348
do
    count=-1

    curl -s "http://www.ebi.ac.uk/ena/data/warehouse/filereport?accession=${study_accession}&result=read_run&fields=secondary_sample_accession,submitted_ftp" | grep -v "^secondary_sample_accession" > ${study_accession}.details.txt

    for fq in `awk '{print $1, $2}' ${study_accession}.details.txt`
    do
        ((count++))
        if [[ $(( count % 2)) -eq 0 ]]
        then
            id=$fq
            current_path=${study_accession}/${id}
            current_base=${current_path}/${id}

            if [ -d "${current_path}" ]; then
                continue
            fi
            echo "Fetching ${id}..."

            mkdir -p ${current_path}
            curl -s "http://www.ebi.ac.uk/ena/data/view/${id}&display=xml" > ${current_base}.xml &
        else
            if [ -e "${current_base}.fna" ]; then
                continue
            fi

            # sed from http://stackoverflow.com/a/10359425/19741
            curl -s $fq | zcat > ${current_base}.fq &
        fi

        if [[ $((count % 10)) -eq 0 ]]
        then
            wait
        fi
    done
done

wait

