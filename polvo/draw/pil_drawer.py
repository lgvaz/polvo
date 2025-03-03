# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/20f_draw.pil_drawer.ipynb.

# %% auto 0
__all__ = ['PILDrawer']

# %% ../../nbs/20f_draw.pil_drawer.ipynb 3
from fastcore.all import *
import polvo as pv
import polvo.bbox as pb

# %% ../../nbs/20f_draw.pil_drawer.ipynb 4
class PILDrawer(pv.Visitor):
    def draw(self, record, image=None, kwargs_list=None):
        self._image = image
        self.visit_all(record, kwargs_list=kwargs_list)
        return self._image
    
    def _visit_image_file(self, image_file, **kwargs): self._image = image_file.open(**kwargs)
    def _visit_bbox(self, bbox, **kwargs): self._image = pb.overlay(bbox=bbox, image=self._image, **kwargs)
    def _visit_bbox_labelled(self, bbox, **kwargs): self._image = pb.overlay_bbox_labelled(bbox=bbox, image=self._image, **kwargs)
    def _visit_obbox(self, obbox, **kwargs): return self._visit_bbox(obbox, **kwargs)
    def _visit_obbox_labelled(self, obbox, **kwargs): return self._visit_bbox_labelled(obbox, **kwargs)
