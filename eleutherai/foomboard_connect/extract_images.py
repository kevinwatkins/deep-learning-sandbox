import sys, json, base64, os.path

outdir = sys.argv[1]

with open('out.ipynb', 'r') as f:
    j = json.load(f)

outs = [o['data']['image/png']
    for c in j['cells']
    if c['cell_type'] == 'code'
    for o in c['outputs']
    if o['output_type'] == 'display_data'
    if 'image/png' in o['data']
]

manifest = []

def save_image(name, index):
    if index >= len(outs):
        return
    manifest.append(name + '\n')
    with open(os.path.join(outdir, name), 'wb') as f:
        f.write(base64.b64decode(outs[index]))

save_image('table.png', 0)
save_image('plot.png', 1)

with open(os.path.join(outdir, "MANIFEST"), 'w') as f:
    f.writelines(manifest)