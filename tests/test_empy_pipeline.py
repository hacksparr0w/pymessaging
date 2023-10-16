import pytest

from pymessaging import Message, Pipeline, PipelineDirection


def test_empty_pipeline():
    pipeline = Pipeline([])

    with pytest.raises(NotImplementedError):
        pipeline.dispatch(Message(), PipelineDirection.BACKWARD)

    with pytest.raises(NotImplementedError):
        pipeline.dispatch(Message(), PipelineDirection.FORWARD)
