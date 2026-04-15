from django.core.exceptions import ValidationError

def valited_file_size(file):



    max_size = 50
    min_size = max_size * 1024 * 1024

    if file.size > max_size:
        raise ValidationError(f"File can not be larger than {max_size} kb")