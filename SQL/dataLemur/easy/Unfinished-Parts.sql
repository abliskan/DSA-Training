SELECT DISTINCT part,
       assembly_step
FROM parts_assembly
where finish_date IS NULL;