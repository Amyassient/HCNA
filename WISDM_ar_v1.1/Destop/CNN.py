
import numpy as np
import tensorflow as tf
import tensorboard
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing


Train_labels = np.loadtxt("./train_labels")
Train_data = np.loadtxt("./train_data")
Train_data = np.reshape(Train_data,(8546,10,10,3))
Train_labels = np.reshape(Train_labels,(8546,6))

Test_labels = np.loadtxt("./test_labels")
Test_data = np.loadtxt("./test_data")
Test_data = np.reshape(Test_data,(2248,10,10,3))
Test_labels = np.reshape(Test_labels,(2248,6))

input_height = 10
input_width = 10
num_labels = 6
num_channels = 3

batch_size = 10
kernel_size = 60
depth = 60
num_hidden = 1000

learning_rate = 0.00001
training_epochs = 10000

#def CNN(input_tensor, train, regularizer):
def CNN(input_tensor, train):
    with tf.variable_scope('layer1-conv1'):
        conv1_weights = tf.get_variable("weight",[3,3,3,60],initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv1_biases = tf.get_variable("bias",[60],initializer=tf.constant_initializer(0.0))
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1,1,1,1],padding='SAME')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))
    with tf.name_scope('layer2-pool1'):
        pool1 = tf.nn.max_pool(relu1, ksize=[1,2,2,1],strides=[1,1,1,1],padding="SAME")
        print(pool1.shape)
    with tf.variable_scope('layer3-conv2'):
        conv2_weights = tf.get_variable("weight",[5,5,60,10],initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv2_biases = tf.get_variable("bias",[10],initializer=tf.constant_initializer(0.0))
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1,1,1,1],padding='VALID')
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))
    with tf.variable_scope('layer4-fc1'):
        pool_shape = relu2.get_shape().as_list()
        nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
        reshaped = tf.reshape(relu2, [-1, nodes])
        print("nodes:", nodes)

        fc1_weights = tf.get_variable("weight",[nodes,1000],initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('loss', regularizer(fc1_weights))
        fc1_biases = tf.get_variable("bias", [1000], initializer=tf.constant_initializer(0.1))
        fc1 = tf.nn.tanh(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        if train:
            fc1 = tf.nn.dropout(fc1, 0.5)
    with tf.variable_scope('layer5-fc2'):
        fc2_weights = tf.get_variable("weight", [1000,6],initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('loss', regularizer(fc2_weights))
        fc2_biases = tf.get_variable("bias", [6], initializer=tf.constant_initializer(0.1))
        logits = tf.nn.softmax(tf.matmul(fc1, fc2_weights) + fc2_biases)
    return logits

X = tf.placeholder(tf.float32, shape=[None,input_height,input_width,num_channels])
Y = tf.placeholder(tf.float32, shape=[None,num_labels])
tf.summary.image('input',Train_data, 20)
regularizer = tf.contrib.layers.l2_regularizer(0.1)
y_ = CNN(X,False)
#loss = -tf.reduce_sum(Y*tf.log(y_))
loss = tf.reduce_sum(tf.nn.sigmoid_cross_entropy_with_logits(labels=Y,logits=y_))
#tf.summary.scalar('loss', loss)

#loss =  tf.nn.softmax_cross_entropy_with_logits(labels=Y,logits=y_)
#global_step = tf.Variable(0)


#loss=tf.reduce_mean(tf.reduce_sum(tf.square(y_ - Y)))
#optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)
#learning_rate = tf.train.exponential_decay(0.01, global_step, 1, 0.9, staircase=True)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)
correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(Y, 1))



accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
tf.summary.scalar('accuracy', accuracy)
with tf.Session() as session:
    tf.initialize_all_variables().run()
    merged = tf.summary.merge_all()
    #train_writer = tf.summary.FileWriter('./train', session.graph)
    #test_writer = tf.summary.FileWriter('./test')
    for i in range(training_epochs):
        #start = (epoch * 60) % 6000
        #end = min(start+60, 6000)
        _, tra_, losss = session.run([optimizer, accuracy, loss], feed_dict={X: Train_data, Y: Train_labels})
        #train_writer.add_summary(summary, epoch)
        _, y_pred, testa = session.run([optimizer, y_, accuracy], feed_dict={X: Test_data, Y: Test_labels})
        #test_writer.add_summary(summary, epoch)
        if(i%10 ==0): 
            y_pred = np.argmax(y_pred, 1)
            y_true = np.argmax(Test_labels, 1)
            C=confusion_matrix(y_true, y_pred)
            print(C)
            print(classification_report(y_true, y_pred))

            print ("step %d, \tTrain: %g, \tTest: %g ce=%g."%(i, tra_, testa, losss))
        #print("Epoch: ", epoch, "Loss:", losss, " Training Accuracy: ",tra_, "Testing:", testa)
        #print("Epoch: ", epoch, " Training Accuracy: ",session.run(accuracy, feed_dict={X: Train_data, Y: Train_labels}))
        #print("Testing Accuracy:", session.run(accuracy, feed_dict={X: Test_data, Y: Test_labels}))
