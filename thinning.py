def thinning(self,image):
        iter = 0
        lb, ti = np.shape(image)
        lb = lb - 1
        ti = ti - 1

        M = np.zeros(image.shape, np.uint8)
        for i in range(1, lb):
            for j in range(1, ti):
                # neighbour matrix,
                p2 = image[i - 1, j]
                p3 = image[i - 1, j + 1]
                p4 = image[i, j + 1]
                p5 = image[i + 1, j + 1]
                p6 = image[i + 1, j]
                p7 = image[i + 1, j - 1]
                p8 = image[i, j - 1]
                p9 = image[i - 1, j - 1]

                a1 = p2 / 255
                a2 = p3 / 255
                a3 = p4 / 255
                a4 = p5 / 255
                a5 = p6 / 255
                a6 = p7 / 255
                a7 = p8 / 255
                a8 = p9 / 255

                # connection
                c1 = 0  # p2 == 0 & & p3 == 1
                c2 = 0  # p3 == 0 & & p4 == 1
                c3 = 0  # p4 == 0 & & p5 == 1
                c4 = 0  # p5 == 0 & & p6 == 1
                c5 = 0  # p6 == 0 & & p7 == 1
                c6 = 0  # p7 == 0 & & p8 == 1
                c7 = 0  # p8 == 0 & & p9 == 1
                c8 = 0  # p9 == 0 & & p2 == 1

                if (p2 == 0 and p3 == 255):
                    c1 = 1
                if (p3 == 0 and p4 == 255):
                    c2 = 1
                if (p4 == 0 and p5 == 255):
                    c3 = 1
                if (p5 == 0 and p6 == 255):
                    c4 = 1
                if (p6 == 0 and p7 == 255):
                    c5 = 1
                if (p7 == 0 and p8 == 255):
                    c6 = 1
                if (p8 == 0 and p9 == 255):
                    c7 = 1
                if (p9 == 0 and p2 == 255):
                    c8 = 1

                A = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8  # connection
                B = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8  # neighbour pixel, black pixel

                iterMod = iter % 2

                # condition 3 and 4
                if (iterMod == 1):
                    m1 = p2 * p4 * p6
                else:
                    m1 = p2 * p4 * p8

                if (iterMod == 1):
                    m2 = p4 * p6 * p8
                else:
                    m2 = p2 * p6 * p8

                iter = iter + 1

                # checking
                if (A == 1 and (B >= 2 and B <= 6) and m1 == 0 and m2 == 0):
                    M[i, j] = 255

            img_thin = cv2.add(image, M)
            
        return img_thin
