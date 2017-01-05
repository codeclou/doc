#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import jinja2


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


svgs = [
    #
    # NON ROOT
    #
    {
        'filename': 'docker-run-as-non-root.svg',
        'first':  { 'name': 'run as', 'width': 48 },
        'second': { 'name': 'non-root', 'width': 60, 'color': '#40B45B' },
    },
    #
    # FROM
    #
    {
        'filename': 'docker-from-alpine-3.5.svg',
        'first':  { 'name': 'from', 'width': 40 },
        'second': { 'name': 'alpine 3.5', 'width': 65, 'color': '#627FFF' },
    },
    {
        'filename': 'docker-from-ubuntu-16.04.svg',
        'first':  { 'name': 'from', 'width': 40 },
        'second': { 'name': 'ubuntu 16.04', 'width': 85, 'color': '#627FFF' },
    },
]
for svg in svgs:
    svgcode = render('svg-badge-template.jinja2', svg)
    f = open('/pyapp/data/' + svg['filename'], 'w+')
    f.write(svgcode)
    f.close()
    print 'writing ' + svg['filename']


#
# DOCKER IMAGE SIZE
#
for number in list(range(12, 60)):
    svgcode = render('svg-badge-template.jinja2', {
        'first':  { 'name': 'image', 'width': 50 },
        'second': { 'name': str(number) + ' MB', 'width': 44, 'color': '#627FFF' },
    })
    docker_image_size_filename = 'docker-image-size-' + str(number) + '.svg'
    f = open('/pyapp/data/' + docker_image_size_filename , 'w+')
    f.write(svgcode)
    f.close()
    print 'writing ' + docker_image_size_filename
    svgs.append({ 'filename': docker_image_size_filename })

for number in list(range(190, 230)):
    svgcode = render('svg-badge-template.jinja2', {
        'first':  { 'name': 'image', 'width': 50 },
        'second': { 'name': str(number) + ' MB', 'width': 55, 'color': '#627FFF' },
    })
    docker_image_size_filename = 'docker-image-size-' + str(number) + '.svg'
    f = open('/pyapp/data/' + docker_image_size_filename , 'w+')
    f.write(svgcode)
    f.close()
    print 'writing ' + docker_image_size_filename
    svgs.append({ 'filename': docker_image_size_filename })

#
# HTML SUMMARY
#
overview = open('/pyapp/data/index.html', 'w+')
overviewcode = render('html-overview.jinja2', { 'svgs': svgs })
overview.write(overviewcode)
overview.close()

print 'done'



