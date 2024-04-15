from pywa import WhatsApp

wa = WhatsApp(phone_id="256226997571281", token='EAAFaFIJHIucBO0cI23YpBZCwZAOXL4zMudkucwubsQuRWPHc1GRl48amLoLXdGEzqdwdnqN5yxvROSmbmdyqTZCiZBEpEQwJjeHvQbRhv9uUyiAQNeADWoADSFs9ObqirFo6CLF5J8NDPAAoQdogzxZAMZCJTvXAKODLIHYjQDyNOkD2DVCuD7jKUz');

jj = wa.upload_media(
    media='./sim.mp4',
    mime_type='video/mp4',
    filename="bamsi"
)
print(wa.send_video(
    to='917710285988',
    video=jj
))