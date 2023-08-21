import tensorflow as tf
import numpy as np
import io
import PIL.Image


class Logger(object):
    def __init__(self, log_dir):
        self.writer = tf.summary.create_file_writer(log_dir)

    def scalar_summary(self, tag, value, step):
        with self.writer.as_default():
            tf.summary.scalar(tag, value, step=step)

    def image_summary(self, tag, images, step):
        with self.writer.as_default():
            image_summaries = []
            for i, img in enumerate(images):
                # Convert image to PIL Image object
                pil_img = PIL.Image.fromarray(img)

                # Create a BytesIO object to store the image data
                image_buffer = io.BytesIO()
                pil_img.save(image_buffer, format='PNG')

                # Create an Image Tensor
                img_tensor = tf.image.decode_image(image_buffer.getvalue(), channels=4)

                # Add image summary
                image_summaries.append(tf.summary.image(f'{tag}/{i}', [img_tensor], step=step))

            tf.summary.experimental.write_raw_pb(tf.summary.experimental.serialize_many_summary(image_summaries), step=step)

    def histo_summary(self, tag, values, step, bins=1000):
        with self.writer.as_default():
            tf.summary.histogram(tag, values, step=step, buckets=bins)