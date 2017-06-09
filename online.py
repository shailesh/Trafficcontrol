import tensorflow as tf, sys
import cv2
import numpy as np
import time
import subprocess

vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()

count = 0
success = True

# cv2.imshow('video', image)

while success:
    # print('Read a new frame: ', count, success)

    if count % 30 == 0:
        cv2.imwrite("./video/images/" + "frame%d.jpg" % count, image)     # save frame as JPEG file

        path = "./video/images/" + "frame" + str(count) + ".jpg"
        print(path)
        print('Read a new frame: ', count, success)
        image_path = path

        # # Read in the image_data
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()

        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line
                           in tf.gfile.GFile("retrained_labels.txt")]

        # Unpersists graph from file
        with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

            predictions = sess.run(softmax_tensor, \
                     {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            print(top_k)

            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                print('%s (score = %.5f)' % (human_string, score))

                if human_string == "vehicle with no parking symbol" and (score * 100) >= 45:
                    print("Please Do Not Park Here")
                    subprocess.call(["afplay", "audio/no-parking.wav"])
                elif human_string == "vehicle on stop line" and (score * 100) >= 45:
                    print("Please Stay Behind Crossing Line")
                    subprocess.call(["afplay", "audio/crossing.wav"])


    count += 1

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

vidcap.release()
out.release()
cv2.destroyAllWindows()
