<h1>Real-time Human face detection using OpenCV</h1>

<h2>Overview</h2>
<p>In this module we will detect human face using <b>HaarCascade Classifier</b>.<br>
We will capture the live video using camera and then the classifier will detect any human face appears in front of camera.<br>
And then we will outline the face with a rectangle.<br><br>
<b>Note:</b> Here, we are only detecting human faces but not recognising them.</p>

<h2>Dependencies</h2>
<p><ul>
    <li>OpenCV</li>
    <li>Numpy</li>
</ul></p>
<p>Use <b>pip</b> to install any missing dependencies.</p>

<h2>Code-Walkthrough</h2>
<ol>
<li>Importing required libraries.</li>
<li>Creating Window and Capturing Live Video using camera.</li>
<li>Using <b>HaarCascade Classifier</b> to detect face.</li>
<li>Outlining face(s) by rectangle using coordinates of face.</li>
<li>Destroying all windows and releasing camera.</li>
</ol>
