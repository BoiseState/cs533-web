"""
Sphinx extension to implement video support
"""

import warnings
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_id
import srt

_vid_root = Path('videos')


def rst_video_tab(video_id, length=None, title='Video', amara=None):
    vcc = nodes.container("", type="tabbed", new_group=False, selected=False, classes=["tabbed-container", "video"])
    if length:
        title += f" ({length})"
    vl = nodes.rubric("Video", title, classes=["tabbed-label"])
    vcc += vl
    vc = nodes.container("", is_div=True, classes=["tabbed-content", "player"])

    vid = nodes.raw('', f"""
<div class="video-container video-embed">
<iframe src="https://boisestate.hosted.panopto.com/Panopto/Pages/Embed.aspx?id={video_id}&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
</div>
    """.strip(), format='html')
    vc += vid
    vcc += vc

    if amara:
        vl = nodes.paragraph("", classes=['aux-links'])
        amr = nodes.reference('', '', classes=['amara'], internal=False)
        amr['refuri'] = amara
        amr += nodes.inline('', 'Edit subtitles on Amara')
        vl += amr
        vc += vl

    return vcc


def rst_slide_tab(slide_id, slide_auth):
    scc = nodes.container("", type="tabbed", new_group=False, selected=False, classes=["tabbed-container", "slides"])
    sl = nodes.rubric("Slides", "Slides", classes=["tabbed-label"])
    scc += sl
    sc = nodes.container("", is_div=True, classes=["tabbed-content", "slides"])

    sid = nodes.raw('', f"""
<div class=slide-container data-id="{slide_id}" data-key={slide_auth}>
</div>
    """.strip(), format='html')
    sc += sid
    scc += sc
    return scc


class VideoDirective(SphinxDirective):
    option_spec = {
        'id': directives.unchanged,
        'slide-id': directives.unchanged,
        'slide-auth': directives.unchanged,
        'length': directives.unchanged,
        'name': directives.path,
        'amara': directives.path,
        'alt-id': directives.unchanged,
        'alt-title': directives.unchanged,
        'alt-amara': directives.path,
    }
    has_content = True
    required_arguments = 0
    optional_arguments = 1

    def _get_video(self):
        name = self.options.get('name', None)
        if name:
            dom = self.env.get_domain('res')
            return dom.lookup_video(name)

    def _get_param(self, name, inv_name):
        res = self.options.get(name, None)
        if not res:
            vid = self._get_video()
            if vid:
                res = vid[inv_name]

        return res

    def run(self):
        result = []

        name = self.options.get('name', None)
        video_id = self._get_param('id', 'Panopto ID')
        length = self.options.get('length', None)
        key = None
        if self.arguments:
            key = self.arguments[0].strip()
        if not key:
            key = make_id(self.env, self.state.document, 'video', name)

        dom = self.env.get_domain('res')

        if video_id:
            tgt_node = nodes.target('', '', ids=[video_id])
            self.set_source_info(tgt_node)
            result.append(tgt_node)
            dom.note_video(key, video_id, name, length)
        else:
            w = self.state.reporter.error(f'Video name {name} has no video ID')
            result.append(w)

        box = nodes.container('', classes=["resource", "video"])
        result.append(box)

        if video_id:
            box += rst_video_tab(video_id, length, amara=self._get_param('amara', 'Amara URL'))

        slide_id = self._get_param('slide-id', 'Slide ID')
        if slide_id:
            slide_auth = self._get_param('slide-auth', 'Slide Auth')
            box += rst_slide_tab(slide_id, slide_auth)

        alt_id = self.options.get('alt-id', None)
        if alt_id:
            box += rst_video_tab(alt_id, title=self.options['alt-title'], amara=self.options.get('alt-amara', None))

        if self.content:
            rcc = nodes.container("", type="tabbed", new_group=False, selected=False,
                                  classes=["tabbed-container"])
            rl = nodes.rubric("Resources and Links", "Resources and Links", classes=["tabbed-label"])
            rcc += rl
            rc = nodes.container("", is_div=True, classes=["tabbed-content", "resources"])
            self.state.nested_parse(self.content, self.content_offset, rc)

            rcc += rc
            box += rcc

        if name:
            tfile = _vid_root / f'{name}.slides.txt'
            if tfile.exists():
                text = tfile.read_text(encoding='utf8')
                hid = nodes.container('', is_div=True, classes=['slides', 'text', 'hidden'])
                tn = nodes.Text(text)
                hid += tn
                box += hid

            sffile = _vid_root / f'{name}.srt'
            if sffile.exists():
                subs = srt.parse(sffile.read_text(encoding='utf8'))
                hid = nodes.container('', is_div=True, classes=['captions', 'text', 'hidden'])
                kids = nodes.bullet_list()
                for sub in subs:
                    tn = nodes.Text(sub.content)
                    kids += nodes.list_item('', tn)
                hid += kids
                box += hid
            else:
                w = self.state.reporter.warning(f'Video file {name}.srt does not exist')
                result.append(w)

        return result
