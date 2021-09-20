#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

try:
    from cmk.gui.plugins.metrics.check_mk import df_translation
except ImportError:
    pass

check_metrics["check_mk-emcunity_pool"]			= df_translation
check_metrics["check_mk-emcunity_lun"]				= df_translation
check_metrics["check_mk-emcunity_fs"]				= df_translation
check_metrics["check_mk-emcunity_vmfs"]				= df_translation
