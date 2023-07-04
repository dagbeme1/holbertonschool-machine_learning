#!/usr/bin/env python3
"""
L2 Regularization Cost
"""
import tensorflow as tf


def l2_reg_cost(cost):
    """
    Function that calculates the cost of a neural network
    with L2 regularization.

    Arguments:
    - cost: TensorFlowscalar representing original cost without regularization

    Returns:
    - TensorFlow scalar representing the cost with L2 regularization.
    """

    # Get the regularization losses
    regularization_losses = tf.losses.get_regularization_losses()

    # Add the regularization losses to the original cost
    cost_with_regularization = cost + tf.reduce_sum(regularization_losses)

    return cost_with_regularization
