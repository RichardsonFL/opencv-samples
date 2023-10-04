# Work with Color filtering

This exemple was made with filtering color from the image. but it can be done from the both video file or video form a camera...

For this example, we have worked with the follow methods:

1. **cvt.cvtColor**, to convert from BRG to RGB color system.

2. **cv2.inRange**, to build an **image mask** which will be used to concatenate with te original image and compose the resulting image. This function take three basic parameter: a source image **MatLike** and two another paramenter that estabilish a limit of color.
    -- That say: `[23,54,100]` to `[170, 156, 200]`

3. **cv2.bitwase_and**, this is to build our result.

All the MatLike result can be shown on preview window or save directily to the file.

## What can we improve in this exemple?

The **threshold array** can be set up to dinamically values. For example, set up to pass it on runtime by pass as the argument of function...