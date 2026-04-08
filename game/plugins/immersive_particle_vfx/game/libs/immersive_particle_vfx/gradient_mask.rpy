################################################################################
##
## Immersive Particle VFX for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.1
## https://feniksdev.itch.io/immersive-particle-vfx-for-renpy
##
################################################################################
## This file contains the base code for two masking shaders that can be used
## to create gradient AlphaMasks for particle animations (or whatever else
## you like).
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
## This tool also comes with assets from several artists. The folders with their
## art is labelled and comes with a credits.txt file so you can credit them
## if you use their work alongside this code.
##
## If you'd like to see how to use this tool, check the other file,
## particle_examples.rpy! This is just the backend; you don't need to
## understand everything in this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
init -999 python:
    renpy.register_shader("feniks.border_gradient", variables="""
        uniform float u_left_border;
        uniform float u_right_border;
        uniform float u_top_border;
        uniform float u_bottom_border;
        uniform vec2 u_my_size;

        uniform vec2 u_model_size;
        attribute vec4 a_position;
        varying vec2 v_coords;
    """, vertex_300="""
        v_coords = vec2(a_position.x / u_model_size.x, a_position.y / u_model_size.y);
    """, fragment_300="""
        vec2 model_size = u_my_size;
        vec2 uv = v_coords;

        float left_border = u_left_border / model_size.x;
        float right_border = u_right_border / model_size.x;
        float top_border = u_top_border / model_size.y;
        float bottom_border = u_bottom_border / model_size.y;

        float alpha = 1.0;
        if (uv.x < left_border) {
            alpha *= uv.x / left_border;
        } else if (uv.x > 1.0 - right_border) {
            alpha *= (1.0 - uv.x) / right_border;
        }
        if (uv.y < top_border) {
            alpha *= uv.y / top_border;
        } else if (uv.y > 1.0 - bottom_border) {
            alpha *= (1.0 - uv.y) / bottom_border;
        }
        alpha = smoothstep(0.0, 1.0, alpha);
        gl_FragColor = vec4(alpha);
    """)
    renpy.register_shader("feniks.radius_gradient", variables="""
        uniform float u_width;
        uniform vec2 u_my_size;

        uniform vec2 u_model_size;
        attribute vec4 a_position;
        varying vec2 v_coords;
    """, vertex_300="""
        v_coords = vec2(a_position.x / u_model_size.x, a_position.y / u_model_size.y);
    """, fragment_300="""
        vec2 model_size = u_my_size;
        vec2 uv = v_coords;

        float width = u_width / model_size.x;
        float radius = max(model_size.x, model_size.y)/2.0;
        radius /= max(model_size.x, model_size.y);
        radius -= width;
        float alpha = 1.0;
        vec2 center = vec2(0.5, 0.5);
        float dist = distance(uv, center);
        if (dist > radius) {
            alpha *= 1.0 - smoothstep(radius, radius + width, dist);
        }
        alpha = smoothstep(0.0, 1.0, alpha);
        gl_FragColor = vec4(alpha);
    """)

    def create_gradient_mask(image, borders, xysize):
        """Add gradient alpha edges to the border of the supplied image."""
        if isinstance(borders, tuple):
            if len(borders) == 4:
                left_border, right_border, top_border, bottom_border = borders
            elif len(borders) == 2:
                left_border = right_border = borders[0]
                top_border = bottom_border = borders[1]
            else:
                raise ValueError("Invalid borders tuple length")
        else:
            left_border = right_border = top_border = bottom_border = borders
        left_border = particle_vfx.compute_raw(left_border, xysize[0])
        right_border = particle_vfx.compute_raw(right_border, xysize[0])
        top_border = particle_vfx.compute_raw(top_border, xysize[1])
        bottom_border = particle_vfx.compute_raw(bottom_border, xysize[1])
        return At(image, gradient_mask(left_border, right_border, top_border, bottom_border, xysize))

    def create_radius_mask(image, width, xysize):
        """Add a circular gradient alpha mask to the supplied image."""
        width = particle_vfx.compute_raw(width, min(*xysize))
        return At(image, gradient_circle_mask(width, xysize))

transform gradient_mask(left_border=0, right_border=0, top_border=0,
        bottom_border=0, xysize=(0, 0)):
    shader "feniks.border_gradient"
    u_left_border left_border
    u_right_border right_border
    u_top_border top_border
    u_bottom_border bottom_border
    u_my_size xysize
transform gradient_circle_mask(width, xysize=(0, 0)):
    shader "feniks.radius_gradient"
    u_width width
    u_my_size xysize

