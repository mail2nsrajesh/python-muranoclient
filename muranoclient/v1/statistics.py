#    Copyright (c) 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from muranoclient.common import base


class Statistic(base.Resource):
    def __repr__(self):
        return "<Statistics %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class StatisticsManager(base.Manager):
    resource_class = Statistic

    def list(self):
        return self._list('/stats', 'stats')