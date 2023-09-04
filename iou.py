    # Filter the results to only grab the car / truck bounding boxes
car_boxes = get_car_boxes(r['rois'], r['class_ids'])

    # See how much cars overlap with the known parking spaces
overlaps = mrcnn.utils.compute_overlaps(car_boxes, parking_areas)
print(overlaps)