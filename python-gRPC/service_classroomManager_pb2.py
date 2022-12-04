# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service-classroomManager.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservice-classroomManager.proto\"\x10\n\x02id\x12\n\n\x02id\x18\x01 \x01(\t\"\x1e\n\x0fGenericResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"%\n\tProfessor\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\"2\n\x11professorResponse\x12\x1d\n\tprofessor\x18\x01 \x01(\x0b\x32\n.Professor\";\n\x19professorsGenericResponse\x12\x1e\n\nprofessors\x18\x01 \x03(\x0b\x32\n.Professor\"3\n\x06\x43ourse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x0f\n\x07horario\x18\x03 \x01(\t\")\n\x0e\x63ourseResponse\x12\x17\n\x06\x63ourse\x18\x01 \x01(\x0b\x32\x07.Course\"2\n\x16\x63oursesGenericResponse\x12\x18\n\x07\x63ourses\x18\x01 \x03(\x0b\x32\x07.Course\"*\n\x07Student\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\x11\n\tmatricula\x18\x02 \x01(\t\",\n\x0fstudentResponse\x12\x19\n\x07student\x18\x01 \x01(\x0b\x32\x08.Student\"5\n\x17studentsGenericResponse\x12\x1a\n\x08students\x18\x01 \x03(\x0b\x32\x08.Student\"\x07\n\x05\x45mpty2\x94\x07\n\x10\x63lassroomManager\x12.\n\x0c\x61\x64\x64Professor\x12\n.Professor\x1a\x10.GenericResponse\"\x00\x12*\n\x0fupdateProfessor\x12\x03.id\x1a\x10.GenericResponse\"\x00\x12*\n\x0f\x64\x65leteProfessor\x12\x03.id\x1a\x10.GenericResponse\"\x00\x12)\n\x0cgetProfessor\x12\x03.id\x1a\x12.professorResponse\"\x00\x12\x35\n\rgetProfessors\x12\x06.Empty\x1a\x1a.professorsGenericResponse\"\x00\x12<\n\x17getProfessorsFromCourse\x12\x03.id\x1a\x1a.professorsGenericResponse\"\x00\x12(\n\taddCourse\x12\x07.Course\x1a\x10.GenericResponse\"\x00\x12\'\n\x0cupdateCourse\x12\x03.id\x1a\x10.GenericResponse\"\x00\x12\'\n\x0c\x64\x65leteCourse\x12\x03.id\x1a\x10.GenericResponse\"\x00\x12#\n\tgetCourse\x12\x03.id\x1a\x0f.courseResponse\"\x00\x12/\n\ngetCourses\x12\x06.Empty\x1a\x17.coursesGenericResponse\"\x00\x12\x39\n\x17getCoursesFromProfessor\x12\x03.id\x1a\x17.coursesGenericResponse\"\x00\x12\x37\n\x15getCoursesFromStudent\x12\x03.id\x1a\x17.coursesGenericResponse\"\x00\x12*\n\naddStudent\x12\x08.Student\x1a\x10.GenericResponse\"\x00\x12(\n\rupdateStudent\x12\x03.id\x1a\x10.GenericResponse\"\x00\x12(\n\rdeleteStudent\x12\x03.id\x1a\x10.GenericResponse\"\x00\x12%\n\ngetStudent\x12\x03.id\x1a\x10.studentResponse\"\x00\x12\x31\n\x0bgetStudents\x12\x06.Empty\x1a\x18.studentsGenericResponse\"\x00\x12\x38\n\x15getStudentsFromCourse\x12\x03.id\x1a\x18.studentsGenericResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_classroomManager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ID._serialized_start=34
  _ID._serialized_end=50
  _GENERICRESPONSE._serialized_start=52
  _GENERICRESPONSE._serialized_end=82
  _PROFESSOR._serialized_start=84
  _PROFESSOR._serialized_end=121
  _PROFESSORRESPONSE._serialized_start=123
  _PROFESSORRESPONSE._serialized_end=173
  _PROFESSORSGENERICRESPONSE._serialized_start=175
  _PROFESSORSGENERICRESPONSE._serialized_end=234
  _COURSE._serialized_start=236
  _COURSE._serialized_end=287
  _COURSERESPONSE._serialized_start=289
  _COURSERESPONSE._serialized_end=330
  _COURSESGENERICRESPONSE._serialized_start=332
  _COURSESGENERICRESPONSE._serialized_end=382
  _STUDENT._serialized_start=384
  _STUDENT._serialized_end=426
  _STUDENTRESPONSE._serialized_start=428
  _STUDENTRESPONSE._serialized_end=472
  _STUDENTSGENERICRESPONSE._serialized_start=474
  _STUDENTSGENERICRESPONSE._serialized_end=527
  _EMPTY._serialized_start=529
  _EMPTY._serialized_end=536
  _CLASSROOMMANAGER._serialized_start=539
  _CLASSROOMMANAGER._serialized_end=1455
# @@protoc_insertion_point(module_scope)