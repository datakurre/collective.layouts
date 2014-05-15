#!/bin/bash

bin/i18ndude rebuild-pot --pot src/collective/layouts/locales/collective.layouts.pot --merge src/collective/layouts/locales/manual.pot --create collective.layouts src/collective/layouts

bin/i18ndude sync --pot src/collective/layouts/locales/collective.layouts.pot src/collective/layouts/locales/*/LC_MESSAGES/collective.layouts.po
