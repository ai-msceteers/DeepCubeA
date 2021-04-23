#!/usr/bin/env sh

for env in cube2 cube3; do
  for weight in 0.0 0.1 0.2 0.3 0.4 0.5 0.6; do
    python3 search_methods/astar.py \
            --states "data/${env}/back100/data_0.pkl" \
            --model "saved_models/${env}/current/" \
            --env "${env}" \
            --weight "${weight}" \
            --batch_size 100 \
            --results_dir "results/${env}weight${weight}/" \
            --language python \
            --nnet_batch_size 100
  done
done
