import sys
import numpy as np
from PyQt5.QtWidgets import QApplication
import pyqtgraph.opengl as gl
from PyQt5.QtGui import QOpenGLShader, QOpenGLShaderProgram

class CustomShaderMesh(gl.GLMeshItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shaderProgram = None
        self.time = 0.0

    def initializeGL(self):
        super().initializeGL()
        self.shaderProgram = QOpenGLShaderProgram()
        
        # Vertex Shader
        vert_shader = """
        attribute vec3 position;
        attribute vec3 normal;
        uniform mat4 mvpMatrix;
        varying vec3 v_normal;
        void main() {
            gl_Position = mvpMatrix * vec4(position, 1.0);
            v_normal = normalize(normal);
        }
        """
        self.shaderProgram.addShaderFromSourceCode(QOpenGLShader.Vertex, vert_shader)

        # Fragment Shader
        frag_shader = """
        varying vec3 v_normal;
        uniform float time;
        void main() {
            float intensity = abs(v_normal.z);
            gl_FragColor = vec4(sin(time)*0.5+0.5, intensity, 1.0-intensity, 1.0);
        }
        """
        self.shaderProgram.addShaderFromSourceCode(QOpenGLShader.Fragment, frag_shader)
        self.shaderProgram.link()

    def paint(self):
        if self.shaderProgram is None:
            self.initializeGL()

        self.shaderProgram.bind()
        self.shaderProgram.setUniformValue("time", self.time)
        self.time += 0.05  # animação simples
        super().paint()
        self.shaderProgram.release()

        
app = QApplication(sys.argv)
view = gl.GLViewWidget()
view.show()

# cria uma malha simples
verts = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])
faces = np.array([
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3]
])

mesh = CustomShaderMesh(vertexes=verts, faces=faces, smooth=False)
view.addItem(mesh)

sys.exit(app.exec_())