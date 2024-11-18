# Generating Test Data
This script generates clusters of monochromatic images and corresponding labels for testing purposes.

## Basic Usage
Generate 3 clusters, randomly selected colors:
```bash
python generate_monochromatic_clusters.py --num-clusters 3 --num-images 50
```

## Specifying Colors
Use specific colors from palette (indices 1, 4, and 7):
```bash
python generate_monochromatic_clusters.py --num-clusters 3 --num-images 50 --color-indices=[1,4,7]
```

## Random Selection with Replacement
Generate 10 clusters allowing repeated colors:
```bash
python generate_monochromatic_clusters.py --num-clusters 10 --num-images 20 --with-replacement
```

## Custom Image Size
Generate 5 clusters with 128x128 images:
```bash
python generate_monochromatic_clusters.py --num-clusters 5 --num-images 30 --size 128
```

## Full Example
Generate 4 clusters, specific colors, custom directory and size:
```bash
python generate_monochromatic_clusters.py \
    --num-clusters 4 \
    --num-images 25 \
    --size 256 \
    --color-indices=[0,3,5,8] \
    --output-dir custom_data \
    --palette colors.palette
```
