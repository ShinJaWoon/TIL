## M:N 관계 

### ManyToManyField

> ```python
> from django.db import models
> 
> class Doctor(models.Model):
>     name = models.TextField()
>     
> class Patient(models.Model):
>     doctors = models.ManyToManyField(Doctor)
>     name = models.TextField()
> ```
>
> - 중개 테이블 명 = <app이름>_patient_doctors
> - Patient는 doctor를 바로 참조 가능하지만, Doctor는 `doctor.patient_set`처럼 역참조를 해야함.
> - doctor와 patient 둘 중 아무 곳에 관계를 선언할 수 있으므로 편한 곳에 선언

### ManyToManyField Arguments

> - related_name
>   - 역참조시 사용할 이름
> - throgh
>   - 중개 테이블을 직접 작성할 경우
> - symmetrical
>   - ManyToManyField가 동일한 모델을 가리킬 때만 사용
>   - source 모델이 target 모델을 참조하면 target 모델도 source 모델을 참조함
>   - 기본 (True) - 역참조 매니저 생성 안됨
>   - 대칭을 원하지 않을 경우 False