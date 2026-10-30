# DeepVariant 1.10.0 with forced realignment windows (--ws_forced_windows_bed,
# --forced_dbg_min_base_quality, --forced_dbg_max_k). Only the Python realigner
# inside make_examples.zip is replaced; native code and models are unchanged.
# Build from the repository root:
#   docker build -f docker/forced_windows/Dockerfile -t deepvariant-forced-windows:1.10.0 .
FROM google/deepvariant:1.10.0
COPY deepvariant/realigner/realigner.py docker/forced_windows/patch_make_examples.py /tmp/forced_windows/
RUN python3 /tmp/forced_windows/patch_make_examples.py --base /opt/deepvariant/bin/make_examples.zip \
        --source /tmp/forced_windows/realigner.py --output /tmp/forced_windows/make_examples.zip \
    && mv /tmp/forced_windows/make_examples.zip /opt/deepvariant/bin/make_examples.zip \
    && rm -rf /tmp/forced_windows
