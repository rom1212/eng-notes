import six
import email
import contextlib
import gzip
import sys

NOT_MULTIPART_TYPE = "text/x-not-multipart"

def decode_binary(blob, encoding='utf-8'):
    # Converts a binary type into a text type using given encoding.
    if isinstance(blob, six.string_types):
        return blob
    return blob.decode(encoding)


def decomp_gzip(data, quiet=True, decode=True):
    try:
        buf = six.BytesIO(encode_text(data))
        with contextlib.closing(gzip.GzipFile(None, "rb", 1, buf)) as gh:
            # E1101 is https://github.com/PyCQA/pylint/issues/1444
            if decode:
                return decode_binary(gh.read())  # pylint: disable=E1101
            else:
                return gh.read()  # pylint: disable=E1101
    except Exception as e:
        if quiet:
            return data
        else:
            raise DecompressionError(six.text_type(e))

def message_from_string(string):
    if sys.version_info[:2] < (2, 7):
        return email.message_from_file(six.StringIO(string))
    return email.message_from_string(string)

def convert_string(raw_data, content_type=NOT_MULTIPART_TYPE):
    if not raw_data:
        raw_data = ''

    def create_binmsg(data, content_type):
        maintype, subtype = content_type.split("/", 1)
        msg = MIMEBase(maintype, subtype)
        msg.set_payload(data)
        return msg

    try:
        data = decode_binary(decomp_gzip(raw_data))
        if "mime-version:" in data[0:4096].lower():
            msg = message_from_string(data)
        else:
            msg = create_binmsg(data, content_type)
    except UnicodeDecodeError:
        msg = create_binmsg(raw_data, content_type)

    return msg

print('good to go')
userdata = b'Content-Type: multipart/mixed; boundary="===============8051749307737749395=="\nMIME-Version: 1.0\n\n--===============8051749307737749395==\nContent-Type: text/x-shellscript; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\nContent-Disposition: attachment; filename="user_data.sh"\n\nIyEvYmluL2Jhc2gKIwojIFRoaXMgc2NyaXB0IGNhcnJpZXMgaW5zaWRlIGl0IG11bHRpcGxlIGZp\nbGVzLiAgV2hlbiBleGVjdXRlZCwgaXQgY3JlYXRlcwojIHRoZSBmaWxlcyBpbnRvIGEgdGVtcG9y\nYXJ5IGRpcmVjdG9yeSBhbmQgdXNlcyB0aGVtIHRvIGV4ZWN1dGUgY29tbWFuZHMKIyB3aGljaCBn\nYXRoZXIgZGF0YSBhYm91dCB0aGUgcnVubmluZyBtYWNoaW5lIG9yIHBlcmZvcm0gYWN0aW9ucy4K\nIwoKIyMjIyBzY3JpcHQgc2V0dXAgIyMjIyMjCmV4cG9ydCBURU1QX0Q9JChta3RlbXAgLWQgIiR7\nVE1QRElSOi0vdG1wfS8kezAjIyovfS5YWFhYWFgiKQpleHBvcnQgQklOX0Q9IiR7VEVNUF9EfS9i\naW4iCmV4cG9ydCBQQVRIPSIkQklOX0Q6L3Vzci9sb2NhbC9zYmluOi91c3IvbG9jYWwvYmluOi91\nc3Ivc2JpbjovdXNyL2Jpbjovc2JpbjovYmluIgoKbWtkaXIgLXAgIiRCSU5fRCIKCiMgRW5zdXJl\nIHRoYXQgaW52b2NhdGlvbnMgb2YgYXB0LWdldCBhcmUgbm90IGludGVyYWN0aXZlIGJ5IGRlZmF1\nbHQsCiMgaGVyZSBhbmQgaW4gYWxsIHN1YnByb2Nlc3Nlcy4KZXhwb3J0IERFQklBTl9GUk9OVEVO\nRD1ub25pbnRlcmFjdGl2ZQoKIyMjIHNvbWUgdXRpbGl0eSBmdW5jdGlvbnMgIyMjIwphcHRnZXQo\nKSB7CiAgICBhcHQtZ2V0IC0tYXNzdW1lLXllcyAtcSAiJEAiIDwvZGV2L251bGwKfQoKYWRkX2Jp\nbigpIHsKICAgIGNhdCA+ICIke0JJTl9EfS8kMSIKICAgIGNobW9kICIkezI6LTc1NX0iICIke0JJ\nTl9EfS8kMSIKfQoKZmFpbCgpIHsKICAgIFsgLXogIiRDUkVEX0NGRyIgXSB8fCBzaWduYWwgRkFJ\nTEVEICIkMSIKICAgIGVjaG8gIkZBSUxFRDogJDEiIDE+JjI7CiAgICBleGl0IDEKfQoKZmluZF9j\ncmVkc19jZmcoKSB7CiAgICBsb2NhbCBjb25maWc9IiIgZmlsZT0iIiBmb3VuZD0iIgoKICAgICMg\nSWYgdGhlIGNvbmZpZyBsb2NhdGlvbiBpcyBzZXQgaW4gZW52aXJvbm1lbnQgdmFyaWFibGUsIHRy\ndXN0IGl0LgogICAgWyAtbiAiJHtDT01NSVNTSU9OSU5HX0NSRURFTlRJQUxTX1VSTH0iIF0gJiYK\nICAgICAgX1JFVD0iJHtDT01NSVNTSU9OSU5HX0NSRURFTlRJQUxTX1VSTH0iICYmIHJldHVybgoK\nICAgICMgR28gbG9va2luZyBmb3IgbG9jYWwgZmlsZXMgd3JpdHRlbiBieSBjbG91ZC1pbml0Lgog\nICAgZm9yIGZpbGUgaW4gL2V0Yy9jbG91ZC9jbG91ZC5jZmcuZC8qY21kbGluZSouY2ZnOyBkbwog\nICAgICAgIFsgLWYgIiRmaWxlIiBdICYmIF9SRVQ9IiRmaWxlIiAmJiByZXR1cm4KICAgIGRvbmUK\nCiAgICBsb2NhbCBvcHQ9IiIgY21kbGluZT0iIgogICAgaWYgWyAtZiAvcHJvYy9jbWRsaW5lIF0g\nJiYgcmVhZCBjbWRsaW5lIDwgL3Byb2MvY21kbGluZTsgdGhlbgogICAgICAgICMgU2VhcmNoIHRo\ncm91Z2ggL3Byb2MvY21kbGluZSBhcmd1bWVudHM6CiAgICAgICAgIyBjbG91ZC1jb25maWctdXJs\nIHRydW1wcyB1cmw9CiAgICAgICAgZm9yIG9wdCBpbiAkY21kbGluZTsgZG8KICAgICAgICAgICAg\nY2FzZSAiJG9wdCIgaW4KICAgICAgICAgICAgICAgIHVybD0qKQogICAgICAgICAgICAgICAgICAg\nIGZvdW5kPSR7b3B0I3VybD19OzsKICAgICAgICAgICAgICAgIGNsb3VkLWNvbmZpZy11cmw9KikK\nICAgICAgICAgICAgICAgICAgICBfUkVUPSIke29wdCMqPX0iCiAgICAgICAgICAgICAgICAgICAg\ncmV0dXJuIDA7OwogICAgICAgICAgICBlc2FjCiAgICAgICAgZG9uZQogICAgICAgIFsgLW4gIiRm\nb3VuZCIgXSAmJiBfUkVUPSIkZm91bmQiICYmIHJldHVybiAwCiAgICBmaQogICAgcmV0dXJuIDEK\nfQoKIyBEbyBldmVyeXRoaW5nIG5lZWRlZCB0byBiZSBhYmxlIHRvIHVzZSBtYWFzX2FwaV9oZWxw\nZXIgb3IgYW55IHNjcmlwdCB3aGljaAojIGltcG9ydHMgaXQuCnByZXBfbWFhc19hcGlfaGVscGVy\nKCkgewogICAgbG9jYWwgY3JlZHM9IiIKCiAgICAjIFVwZGF0ZSBhcHQgY2FjaGUgYW5kIGluc3Rh\nbGwgbGlicmFyaWVzIHJlcXVpcmVkIGJ5IG1hYXNfYXBpX2hlbHBlci5weQogICAgYXB0Z2V0IHVw\nZGF0ZQogICAgYXB0Z2V0IGluc3RhbGwgcHl0aG9uMy15YW1sIHB5dGhvbjMtb2F1dGhsaWIKCiAg\nICBmaW5kX2NyZWRzX2NmZyB8fCBmYWlsICJGYWlsZWQgdG8gZmluZCBjcmVkZW50aWFsIGNvbmZp\nZyIKICAgIGNyZWRzPSIkX1JFVCIKCiAgICAjIEdldCByZW1vdGUgY3JlZGVudGlhbHMgaW50byBh\nIGxvY2FsIGZpbGUuCiAgICBjYXNlICIkY3JlZHMiIGluCiAgICAgICAgaHR0cDovLyp8aHR0cHM6\nLy8qKQogICAgICAgICAgICB3Z2V0ICIkY3JlZHMiIC1PICIke1RFTVBfRH0vbXkuY3JlZHMiIHx8\nCiAgICAgICAgICAgICAgZmFpbCAiZmFpbGVkIHRvIGdldCBjcmVkZW50aWFscyBmcm9tICRjcmVk\nX2NmZyIKICAgICAgICAgICAgY3JlZHM9IiR7VEVNUF9EfS9teS5jcmVkcyIKICAgICAgICAgICAg\nOzsKICAgIGVzYWMKCiAgICAjIFVzZSBnbG9iYWwgbmFtZSByZWFkIGJ5IHNpZ25hbCgpLgogICAg\nZXhwb3J0IENSRURfQ0ZHPSIkY3JlZHMiCn0KCiMgSW52b2tlIHRoZSAic2lnbmFsKCkiIEFQSSBj\nYWxsIHRvIHJlcG9ydCBwcm9ncmVzcy4KIyBVc2FnZTogc2lnbmFsIDxzdGF0dXM+IDxtZXNzYWdl\nPgpzaWduYWwoKSB7CiAgICBtYWFzLXNpZ25hbCAiLS1jb25maWc9JHtDUkVEX0NGR30iICIkQCIK\nfQoKCiMgVGhpcyBzY3JpcHQgaXMgcGFzc2VkIHRvIGNsb3VkLWluaXQgZnJvbSBNQUFTIGR1cmlu\nZyBjb21taXNzaW9uaW5nLiBUaGlzCiMgc2NyaXB0IGNvbnRhaW5zIG11bHRpcGxlIGZpbGVzIGlu\nc2lkZSBpdC4gV2hlbiBleGVjdXRlZCB0aGVzZSBmaWxlcyBhcmUKIyBleHRyYWN0ZWQgYW5kIHJ1\nbi4gVGhpcyBzY3JpcHQgZGV0ZWN0cyBwb3dlciBzZXR0aW5ncywgcnVucyBjb21taXNzaW9uaW5n\nCiMgc2NyaXB0cyB0byBnYXRoZXIgZGF0YSBhYm91dCB0aGUgc3lzdGVtLCBhbmQgcnVucyB0ZXN0\naW5nIHNjcmlwdHMgdG8gdmFsaWRhdGUKIyB0aGUgaGFyZHdhcmUgaXMgaW4gYSBmdW5jdGlvbmlu\nZyBzdGF0ZS4KCiMjIyMgIElQTUkgc2V0dXAgICMjIyMjIwpJUE1JX0NPTkZJR19EPSIke1RFTVBf\nRH0vaXBtaS5kIgpta2RpciAtcCAiJElQTUlfQ09ORklHX0QiCiMgSWYgSVBNSSBuZXR3b3JrIHNl\ndHRpbmdzIGhhdmUgYmVlbiBjb25maWd1cmVkIHN0YXRpY2FsbHksIHlvdSBjYW4KIyBtYWtlIHRo\nZW0gREhDUC4gSWYgJ3RydWUnLCB0aGUgSVBNSSBuZXR3b3JrIHNvdXJjZSB3aWxsIGJlIGNoYW5n\nZWQKIyB0byBESENQLgpJUE1JX0NIQU5HRV9TVEFUSUNfVE9fREhDUD0iZmFsc2UiCgojIEluIGNl\ncnRhaW4gaGFyZHdhcmUsIHRoZSBwYXJhbWV0ZXJzIGZvciB0aGUgaXBtaV9zaSBrZXJuZWwgbW9k\ndWxlCiMgbWlnaHQgbmVlZCB0byBiZSBzcGVjaWZpZWQuIElmIHlvdSB3aXNoIHRvIHNlbmQgcGFy\nYW1ldGVycywgdW5jb21tZW50CiMgdGhlIGZvbGxvd2luZyBsaW5lLgojSVBNSV9TSV9QQVJBTVM9\nInR5cGU9a2NzIHBvcnRzPTB4Y2EyIgoKYWRkX2lwbWlfY29uZmlnKCkgewogICBjYXQgPiAiJHtJ\nUE1JX0NPTkZJR19EfS8kMSIKICAgY2htb2QgIiR7MjotNjQ0fSIgIiR7SVBNSV9DT05GSUdfRH0v\nJDEiCn0KCm1haW4oKSB7CiAgICBwcmVwX21hYXNfYXBpX2hlbHBlcgoKICAgICMgSW5zdGFsbCBJ\nUE1JIGRlcHMKICAgIGFwdGdldCBpbnN0YWxsIGZyZWVpcG1pLXRvb2xzIG9wZW5pcG1pIGlwbWl0\nb29sIHNzaHBhc3MKCiAgICAjIExvYWQgSVBNSSBrZXJuZWwgbW9kdWxlcwogICAgbW9kcHJvYmUg\naXBtaV9tc2doYW5kbGVyCiAgICBtb2Rwcm9iZSBpcG1pX2RldmludGYKICAgIG1vZHByb2JlIGlw\nbWlfc2kgJHtJUE1JX1NJX1BBUkFNU30KICAgIG1vZHByb2JlIGlwbWlfc3NpZgogICAgdWRldmFk\nbSBzZXR0bGUKCiAgICAjIFBvd2VyIHNldHRpbmdzLgogICAgbG9jYWwgcGFyZ3M9IiIKICAgIGlm\nICRJUE1JX0NIQU5HRV9TVEFUSUNfVE9fREhDUDsgdGhlbgogICAgICAgIHBhcmdzPSItLWRoY3At\naWYtc3RhdGljIgogICAgZmkKICAgIHBvd2VyX3R5cGU9JChtYWFzLWlwbWktYXV0b2RldGVjdC10\nb29sKQogICAgaWYgWyAteiAkcG93ZXJfdHlwZSBdOyB0aGVuCiAgICAgICAgcG93ZXJfdHlwZT0k\nKG1hYXMtd2VkZ2UtYXV0b2RldGVjdCAtLWNoZWNrKSB8fCBwb3dlcl90eXBlPSIiCiAgICBmaQog\nICAgY2FzZSAiJHBvd2VyX3R5cGUiIGluCiAgICAgICAgaXBtaSkKICAgICAgICAgICAgcG93ZXJf\nc2V0dGluZ3M9JChtYWFzLWlwbWktYXV0b2RldGVjdCBcCiAgICAgICAgICAgICAgLS1jb25maWdk\naXIgIiRJUE1JX0NPTkZJR19EIiAke3BhcmdzfSkKICAgICAgICAgICAgOzsKICAgICAgICBtb29u\nc2hvdCkKICAgICAgICAgICAgcG93ZXJfc2V0dGluZ3M9JChtYWFzLW1vb25zaG90LWF1dG9kZXRl\nY3QpCiAgICAgICAgICAgIDs7CiAgICAgICAgd2VkZ2UpCiAgICAgICAgICAgIHBvd2VyX3NldHRp\nbmdzPSQobWFhcy13ZWRnZS1hdXRvZGV0ZWN0IC0tZ2V0LWNyZWRlbnRpYWxzKSB8fCBwb3dlcl9z\nZXR0aW5ncz0iIgogICAgICAgICAgICA7OwogICAgZXNhYwogICAgaWYgWyAhIC16ICIkcG93ZXJf\nc2V0dGluZ3MiIF07IHRoZW4KICAgICAgICBzaWduYWwgXAogICAgICAgICAgIi0tcG93ZXItdHlw\nZT0ke3Bvd2VyX3R5cGV9IiAiLS1wb3dlci1wYXJhbWV0ZXJzPSR7cG93ZXJfc2V0dGluZ3N9IiBc\nCiAgICAgICAgICBXT1JLSU5HICJGaW5pc2hlZCBbbWFhcy1pcG1pLWF1dG9kZXRlY3RdIgogICAg\nZmkKCiAgICBtYWFzLXJ1bi1yZW1vdGUtc2NyaXB0cyAiLS1jb25maWc9JHtDUkVEX0NGR30iICIk\ne1RFTVBfRH0iCn0KCiMjIyBiZWdpbiB3cml0aW5nIGZpbGVzICMjIwoKIyBFeGFtcGxlIGNvbmZp\nZzogZW5hYmxlIEJNQyByZW1vdGUgYWNjZXNzIChvbiBzb21lIHN5c3RlbXMuKQojYWRkX2lwbWlf\nY29uZmlnICIwMi1nbG9iYWwtY29uZmlnLmlwbWkiIDw8IkVORF9JUE1JX0NPTkZJRyIKI1NlY3Rp\nb24gTGFuX0NoYW5uZWwKIwlWb2xhdGlsZV9BY2Nlc3NfTW9kZQkJCUFsd2F5c19BdmFpbGFibGUK\nIwlWb2xhdGlsZV9FbmFibGVfVXNlcl9MZXZlbF9BdXRoCQlZZXMKIwlWb2xhdGlsZV9DaGFubmVs\nX1ByaXZpbGVnZV9MaW1pdAlBZG1pbmlzdHJhdG9yCiMJTm9uX1ZvbGF0aWxlX0FjY2Vzc19Nb2Rl\nCQlBbHdheXNfQXZhaWxhYmxlCiMJTm9uX1ZvbGF0aWxlX0VuYWJsZV9Vc2VyX0xldmVsX0F1dGgJ\nWWVzCiMJTm9uX1ZvbGF0aWxlX0NoYW5uZWxfUHJpdmlsZWdlX0xpbWl0CUFkbWluaXN0cmF0b3IK\nI0VuZFNlY3Rpb24KI0VORF9JUE1JX0NPTkZJRwoKYWRkX2JpbiAibWFhcy1pcG1pLWF1dG9kZXRl\nY3QtdG9vbCIgPDwiRU5EX01BQVNfSVBNSV9BVVRPREVURUNUX1RPT0wiCiMhL3Vzci9iaW4vcHl0\naG9uMwoKaW1wb3J0IGdsb2IKaW1wb3J0IHJlCmltcG9ydCBzdWJwcm9jZXNzCgoKZGVmIGRldGVj\ndF9pcG1pKCk6CiAgICAjIFhYWDogYW5kcmVzZXJsIDIwMTMtMDQtMDkgYnVnPTEwNjQ1Mjc6IFRy\neSB0byBkZXRlY3QgaWYgbm9kZQogICAgIyBpcyBhIFZpcnR1YWwgTWFjaGluZS4gSWYgaXQgaXMs\nIGRvIG5vdCB0cnkgdG8gZGV0ZWN0IElQTUkuCiAgICB3aXRoIG9wZW4oJy9wcm9jL2NwdWluZm8n\nLCAncicpIGFzIGNwdWluZm86CiAgICAgICAgZm9yIGxpbmUgaW4gY3B1aW5mbzoKICAgICAgICAg'
# \nICAgaWYgbGluZS5zdGFydHN3aXRoKCdtb2RlbCBuYW1lJykgYW5kICdRRU1VJyBpb'

userdata_str = convert_string(userdata)
print('userdata str:', userdata_str)

def fully_decoded_payload(part):
    # In Python 3, decoding the payload will ironically hand us a bytes object.
    # 'decode' means to decode according to Content-Transfer-Encoding, not
    # according to any charset in the Content-Type.  So, if we end up with
    # bytes, first try to decode to str via CT charset, and failing that, try
    # utf-8 using surrogate escapes.
    cte_payload = part.get_payload(decode=True)
    if (six.PY3 and
            part.get_content_maintype() == 'text' and
            isinstance(cte_payload, bytes)):
        charset = part.get_charset()
        if charset and charset.input_codec:
            encoding = charset.input_codec
        else:
            encoding = 'utf-8'
        return cte_payload.decode(encoding, 'surrogateescape')
    return cte_payload


def walk(msg):
    partnum = 0
    for part in msg.walk():
        # multipart/* are just containers
        print('part.get_content_maintype():', part.get_content_maintype())
        if part.get_content_maintype() == 'multipart':
            continue

        ctype = part.get_content_type()
        print('part.get_content_type()', part.get_content_type())
        if ctype is None:
            ctype = OCTET_TYPE

        filename = part.get_filename()
        print('part.get_filename()', part.get_filename())
        if not filename:
            filename = PART_FN_TPL % (partnum)

        payload = fully_decoded_payload(part)
        print('payload:', payload)
        # callback(data, filename, payload, headers)
        # partnum = partnum + 1

walk(userdata_str)
