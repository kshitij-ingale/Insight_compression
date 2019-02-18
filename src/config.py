#!/usr/bin/env python3

class image_properties(object):
    DEPTH = 3                                                 # Dimension of the input image to network corresponding to channels
    HEIGHT = 256                                              # Dimension of the input image to network corresponding to height
    WIDTH = 256                                               # Dimension of the input image to network corresponding to width
    compressed_dims = [1, int(HEIGHT/16), int(WIDTH/16), 10]  # Dimension of the compressed quantized vector
    
class config_train(object):
    
    train_fraction = 0.9                # Train-test split fraction for dataset
    mode = 'gan-train'                  # Mode specify train/test function
    num_epochs = 40                     # Number of epochs for training
    batch_size = 4                      # Batch size for training
    ema_decay = 0.999                   # Decay factor for exponential moving average term for parameters
    G_learning_rate = 2e-4              # Learning rate for generator network
    D_learning_rate = 2e-4              # Learning rate for discriminator network
    diagnostic_steps = 50               # Steps after which model performance is to be evaluated
    
# Compression factors
    perceptual_coeff = 0.2              # Coefficient for perceptual loss
    distortion_coeff = 12               # Coefficient for distortion loss
    channel_bottleneck = 10             # Compression bottleneck
    use_vanilla_GAN = False             # Check if vanilla-GAN loss function is to be used
    use_feature_matching_loss = True    # Check if feature matching loss is to be used (Loss function considering different downsampled images)
    multiscale = True                   # Check if multiscale discriminator is to be used
    feature_matching_weight = 10        # Coefficient for feature matching loss

class config_test(config_train):
    mode = 'gan-test'                   # Mode specify train/test function
    num_epochs = 512
    batch_size = 1

class directories(object):
    train = 'data/paths_train.d5'           # Directory for training dataframe
    test = 'data/paths_test.d5'             # Directory for test dataframe
    tensorboard = 'tensorboard'             # Directory for tensorboard summary
    checkpoints = 'checkpoints'             # Directory for storing checkpoints
    checkpoints_best = 'checkpoints/best'   # Directory for storing checkpoints corresponding to minimum loss values
    samples = 'output/'                     # Directory for output files
    infer = 'hdf_store/infer.d5'
