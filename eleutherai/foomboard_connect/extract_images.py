import sys, json, base64, os.path, mistune

scriptdir = sys.argv[1]
outdir = sys.argv[2]

with open('out.ipynb', 'r') as f:
    j = json.load(f)

outs = [o['data']
    for c in j['cells']
    if c['cell_type'] == 'code'
    for o in c['outputs']
    if o['output_type'] == 'display_data'
    if 'image/png' in o['data']
      or 'text/markdown' in o['data']
]

manifest = []

def save_output_cell(name, index, dtype, wrapper=None):
    if index >= len(outs) or not dtype in outs[index]:
        return
    
    data = outs[index][dtype]
    mode = 'w'
    if dtype == 'text/markdown':
        if isinstance(data, list):
            data = ''.join(data)
        data = mistune.markdown(data)
        if wrapper:
            with open(wrapper, 'r') as f:
                data = f.read().replace('BODY', data)
    elif dtype == 'image/png':
        data = base64.b64decode(data)
        mode = 'wb'
    else:
        return
    
    manifest.append(name + '\n')
    with open(os.path.join(outdir, name), mode) as f:
        f.write(data)

save_output_cell('table.html', 0, 'text/markdown', wrapper=os.path.join(scriptdir, 'table_wrapper.html'))
save_output_cell('plot.png', 1, 'image/png')

with open(os.path.join(outdir, 'MANIFEST'), 'w') as f:
    f.writelines(manifest)