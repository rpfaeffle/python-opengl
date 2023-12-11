from OpenGL.GL import *

class OpenGLUtils(object):

    @staticmethod
    def initialize_shader(shader_code, shader_type):
        # specify required OpenGL version
        shader_code = '#version 330\n' + shader_code

        # Create empty shader object and return reference value
        shader_ref = glCreateShader(shader_type)
        # store source code in shader
        glShaderSource(shader_ref, shader_code)

        # compile source code
        glCompileShader(shader_ref)

        # Make sure compilation was successfull
        compile_success = glGetShaderiv(shader_ref, GL_COMPILE_STATUS)

        if not compile_success:
            error_message = glGetShaderInfoLog(shader_ref)
            # Free memory
            glDeleteShader(shader_ref)
            # convert byte string to human-readable string
            error_message = '' + error_message.decode('utf-8')
            raise Exception(error_message)
        return shader_ref

    @staticmethod
    def initialize_program(vertex_shader_code, fragment_shader_code):
        vertex_shader_ref = OpenGLUtils.initialize_shader(vertex_shader_code, GL_VERTEX_SHADER)
        fragment_shader_code = OpenGLUtils.initialize_shader(fragment_shader_code, GL_FRAGMENT_SHADER)

        program_ref = glCreateProgram()

        # attach previously compiled shader program
        glAttachShader(program_ref, vertex_shader_ref)
        glAttachShader(program_ref, fragment_shader_code)

        # Link vertex shader to fragment shader
        glLinkProgram(program_ref)

        # Check whether linking was successfull
        compile_success = glGetProgramiv(program_ref, GL_LINK_STATUS)

        if not compile_success:
            error_message = glGetShaderInfoLog(program_ref)
            # Free memory
            glDeleteProgram(program_ref)
            # convert byte string to human-readable string
            error_message = '' + error_message.decode('utf-8')
            raise Exception(error_message)
        return program_ref