#  Copyright (c) 2020 - 2023, Arm Limited. All rights reserved.<BR>
class PatchCheckConf:
    ignore_change_id = False

            if not PatchCheckConf.ignore_change_id:
                self.check_change_id_format()
    def check_change_id_format(self):
        cid='Change-Id:'
        if self.msg.find(cid) != -1:
            self.error('\"%s\" found in commit message:' % cid)
            return

                if self.filename.endswith('.rtf'):
                    self.force_crlf = False
                    self.force_notabs = False
                   os.path.basename(self.filename).lower() == 'makefile' or \
                   os.path.splitext(self.filename)[1] == '.makefile' or \
                   self.filename.startswith(
                        'BaseTools/Source/C/VfrCompile/Pccts/'):
            if self.binary or self.filename.endswith(".rtf"):
        rp_file = os.path.realpath(self.filename)
        rp_script = os.path.realpath(__file__)
        if line.find('__FUNCTION__') != -1 and rp_file != rp_script:
            self.added_line_error('__FUNCTION__ was used, but __func__ '
                                  'is now recommended', line)

        group.add_argument("--ignore-change-id",
                           action="store_true",
                           help="Ignore the presence of 'Change-Id:' tags in commit message")
        if self.args.ignore_change_id:
            PatchCheckConf.ignore_change_id = True