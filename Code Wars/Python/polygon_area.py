def area_polygon(vertex):
    #Calculate Products
    #Found Method for Calculating Polygon Area at https://www.wikihow.com/Calculate-the-Area-of-a-Polygon#:~:text=of%20a%20polygon%3F-,Write%20down%20the%20formula%20for%20finding%20the%20area%20of%20a,lengths%20of%20all%20the%20sides
    # & https://www.mathopenref.com/coordpolygonarea.html.
    #X by Trailing Y
    product_sum_x = 0
    product_sum_x1 = 0

    for i in range(len(vertex)):
        if i == 0:
            product_sum_x = 0
        if i > 0 and i < len(vertex):
            product_sum_x = (vertex[i-1][0] * vertex[i][1])/2 + product_sum_x
        if i == len(vertex)-1:
            product_sum_x1 = (vertex[i][0] * vertex[0][1])/2 + product_sum_x
    print(f"The product of Xs and Trailing Ys is: {product_sum_x1}")

    #Y by Trailing X
    product_sum_y = 0
    product_sum_y1 = 0

    for i in range(len(vertex)):
        if i == 0:
            product_sum_y = 0
        if i > 0 and i < len(vertex):
            product_sum_y = (vertex[i][0] * vertex[i-1][1])/2 + product_sum_y
        if i == len(vertex)-1:
            product_sum_y1 = (vertex[0][0] * vertex[i][1])/2 + product_sum_y
    print(f"The product of Ys and Trailing Xs is: {product_sum_y1}")

    print(abs(round(product_sum_y1 - product_sum_x1, 1)))
    return abs(round(product_sum_y1 - product_sum_x1, 1))

area_polygon([(1, 1), (3, 4), (6, 1)])
area_polygon([(1, 3), (3, 3), (3, 1), (1, 1)])
area_polygon([(0, 5), (3, 3), (2, -3), (-2, -3), (-3, 3)])