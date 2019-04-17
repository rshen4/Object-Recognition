1.a the threshold value is 100
1.c Attributes are: area, x_position, y_position, theta_min, theta_max, E_min, E_max
1.d comparison criteria are minimum moment and roundness. The threshold is 0.85

2.b The resolution of theta is set to be pi/800. The voting scheme is that everytime qualified radius and angle (theta) are examed, add one at the corresponding location in the accumulating matrix.     The edge threshold is 20.
2.c The hough threshold is 120.
2.d Algorithm: Start seatching from the most outter edge. Examing points along the edge and if the corresponding point on the edge_threshold_point is 255, then this point is 255. Othereise, recourd 0 for this point.