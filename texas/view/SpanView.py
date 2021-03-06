#!/usr/bin/python
#-*- coding: utf-8 -*-

from .AnnotationView import AnnotationView
from texas.anns.SpanAnnotation import SpanAnnotation

class SpanView(AnnotationView):

    def __init__(self, pName : str, pType : str = None):
        # automatically set type as "SpanView"
        super(SpanView, self).__init__(pName = pName, pType = pType) # pType = "AnnotationView"+"."+"SpanView")
        self.setTexasClass("tx.view.SpanView")

    def add(self,pStartToken:int, pFinalToken:int, pLabel:str = "", pSpan:str = None):
        self.getAnnSet().add ( SpanAnnotation(pStartToken, pFinalToken, pLabel, pSpan) )
